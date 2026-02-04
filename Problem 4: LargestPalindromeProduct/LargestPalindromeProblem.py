import time

startTime = time.perf_counter()

largestPalindrome = 1

for i in range(100, 1000):
    for k in range(100, 1000):
        product = i*k
        if str(product) == str(product)[::-1] and product > largestPalindrome:
                largestPalindrome = product

print(f"The largest palindrome is {largestPalindrome}")

endTime = time.perf_counter()
programRunTime = endTime - startTime
print(f"Program ran for {programRunTime} seconds")