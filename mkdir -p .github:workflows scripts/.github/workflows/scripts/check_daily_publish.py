#!/usr/bin/env python3
"""
Check whether the given author has added files or commits in the past N days.
If none found, create a GitHub issue and add a card to the repository Project board.
If published, add a card to the "Published" column.

Usage (via GitHub Action environment):
  python3 scripts/check_daily_publish.py --author "SenayK-bit" --days 1 --label publish-check \
    --published-column "Published" --missed-column "Missed" --project-name "Publish status" --create-project-if-missing true
"""

import argparse
import os
import subprocess
import json
from urllib import request, parse
from datetime import datetime

GITHUB_API = "https://api.github.com"
INERTIA_ACCEPT = "application/vnd.github.inertia-preview+json"  # required for classic Projects API

def run_git(cmd):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print("git command failed:", cmd)
        print(res.stdout)
        print(res.stderr)
        raise SystemExit(1)
    return res.stdout.strip()

def count_added_files(author, days):
    since = f"{days} days ago"
    cmd = f'git log --since="{since}" --author="{author}" --diff-filter=A --name-only --pretty=format:""'
    out = run_git(cmd)
    files = [line for line in out.splitlines() if line.strip()]
    unique_files = set(files)
    print(f"Found {len(unique_files)} added files by '{author}' in the last {days} day(s).")
    return len(unique_files), sorted(unique_files)

def count_commits(author, days):
    cmd = f'git rev-list --count --since="{days} days ago" --author="{author}" HEAD'
    out = run_git(cmd)
    try:
        return int(out.strip())
    except:
        return 0

# Simple HTTP helpers
def api_request(method, url, token, data=None, accept=None):
    headers = {
        "Accept": accept or "application/vnd.github+json",
        "Authorization": f"token {token}",
        "User-Agent": "daily-publish-check-script"
    }
    body = None
    if data is not None:
        body = json.dumps(data).encode()
        headers["Content-Type"] = "application/json"
    req = request.Request(url, data=body, headers=headers, method=method)
    try:
        with request.urlopen(req) as resp:
            resp_body = resp.read().decode()
            if resp_body:
                return json.loads(resp_body)
            return {}
    except request.HTTPError as e:
        err = e.read().decode()
        print(f"API {method} {url} failed: {e.code} {e.reason} - {err}")
        return None
    except Exception as e:
        print(f"API request error for {url}: {e}")
        return None

# Projects (classic) helpers
def find_or_create_project(owner, repo, project_name, token, create_if_missing=True):
    url = f"{GITHUB_API}/repos/{owner}/{repo}/projects"
    projects = api_request("GET", url, token, accept=INERTIA_ACCEPT)
    if projects is None:
        return None
    for p in projects:
        if p.get("name") == project_name:
            return p
    if not create_if_missing:
        return None
    # create project
    data = {"name": project_name, "body": "Repository publish status board (automatically created)"}
    created = api_request("POST", url, token, data=data, accept=INERTIA_ACCEPT)
    return created

def find_or_create_column(project_id, column_name, token):
    url = f"{GITHUB_API}/projects/{project_id}/columns"
    cols = api_request("GET", url, token, accept=INERTIA_ACCEPT)
    if cols is None:
        return None
    for c in cols:
        if c.get("name") == column_name:
            return c
    data = {"name": column_name}
    created = api_request("POST", url, token, data=data, accept=INERTIA_ACCEPT)
    return created

def list_cards_in_column(column_id, token):
    url = f"{GITHUB_API}/projects/columns/{column_id}/cards"
    return api_request("GET", url, token, accept=INERTIA_ACCEPT) or []

def create_note_card(column_id, note, token):
    url = f"{GITHUB_API}/projects/columns/{column_id}/cards"
    data = {"note": note}
    return api_request("POST", url, token, data=data, accept=INERTIA_ACCEPT)

def create_issue(owner, repo, title, body, token, label=None):
    url = f"{GITHUB_API}/repos/{owner}/{repo}/issues"
    data = {"title": title, "body": body}
    if label:
        data["labels"] = [label]
    return api_request("POST", url, token, data=data)

def close_prev_issues(owner, repo, token, label):
    # Find open issues with the label and close them
    query = parse.quote(f"repo:{owner}/{repo} is:open label:{label}")
    url = f"{GITHUB_API}/search/issues?q={query}"
    data = api_request("GET", url, token)
    if not data:
        return
    for item in data.get("items", []):
        issue_number = item["number"]
        issue_url = f"{GITHUB_API}/repos/{owner}/{repo}/issues/{issue_number}"
        api_request("PATCH", issue_url, token, data={"state":"closed"})

def ensure_card_for_today(column_id, note_text, token):
    # avoid duplicate cards for the same note text (or date prefix)
    cards = list_cards_in_column(column_id, token)
    for c in cards:
        note = c.get("note") or ""
        if note.strip() == note_text.strip():
            print("Card for today already exists in target column.")
            return c
    return create_note_card(column_id, note_text, token)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--author", required=True)
    parser.add_argument("--days", type=int, default=1)
    parser.add_argument("--label", default="publish-check")
    parser.add_argument("--close-issues", choices=["true", "false"], default="false")
    parser.add_argument("--project-name", default="Publish status")
    parser.add_argument("--published-column", default="Published")
    parser.add_argument("--missed-column", default="Missed")
    parser.add_argument("--create-project-if-missing", choices=["true","false"], default="true")
    args = parser.parse_args()

    # tokens
    project_token = os.environ.get("PROJECT_TOKEN") or os.environ.get("GITHUB_TOKEN")
    issue_token = os.environ.get("GITHUB_TOKEN")
    repo_full = os.environ.get("GITHUB_REPOSITORY")
    if not repo_full:
        print("GITHUB_REPOSITORY env var missing (owner/repo). Exiting.")
        raise SystemExit(1)
    owner, repo = repo_full.split("/")

    commits = count_commits(args.author, args.days)
    added_count, files = count_added_files(args.author, args.days)

    today = datetime.utcnow().strftime("%Y-%m-%d")
    if commits > 0 or added_count > 0:
        print(f"OK: Author '{args.author}' published in the last {args.days} day(s). Commits: {commits}, Files added: {added_count}")
        # Optionally close previous missing publish issues
        if issue_token and args.close_issues == "true":
            close_prev_issues(owner, repo, issue_token, args.label)

        # Update project: add a Published card for today
        if project_token:
            project = find_or_create_project(owner, repo, args.project_name, project_token, create_if_missing=(args.create_project_if_missing=="true"))
            if project:
                col = find_or_create_column(project["id"], args.published_column, project_token)
                if col:
                    note = f"{today} — Published by @{args.author}. Commits: {commits}, Files added: {added_count}"
                    ensure_card_for_today(col["id"], note, project_token)
                else:
                    print("Could not find or create published column.")
            else:
                print("Could not find or create project board.")
        return

    # No activity found -> create an issue
    if not issue_token:
        print("No GITHUB_TOKEN; cannot create issue. Exiting with non-zero code.")
        raise SystemExit(1)

    title = f"[Publish check] No publish detected on {today}"
    body_lines = [
        f"Automated check: no commits or newly added files by @{args.author} were detected in the last {args.days} day(s).",
        "",
        "If this is expected you can ignore this issue. If not, please add your files or commit changes."
    ]
    body = "\n".join(body_lines)
    created_issue = create_issue(owner, repo, title, body, issue_token, label=args.label)
    if not created_issue:
        raise SystemExit(1)
    issue_html = created_issue.get("html_url", "")

    # Create/append a card to the Missed column with a link to the issue
    if project_token:
        project = find_or_create_project(owner, repo, args.project_name, project_token, create_if_missing=(args.create_project_if_missing=="true"))
        if project:
            col = find_or_create_column(project["id"], args.missed_column, project_token)
            if col:
                note = f"{today} — Missed publish by @{args.author}. See issue: {issue_html}"
                ensure_card_for_today(col["id"], note, project_token)
            else:
                print("Could not find or create missed column.")
        else:
            print("Could not find or create project board.")

if __name__ == "__main__":
    main()