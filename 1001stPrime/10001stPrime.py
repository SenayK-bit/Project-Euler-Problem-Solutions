primes = {2, 3}
stuff = False
hello = 0

for i in range(4, 100000):
    l = int(i ** 0.5)
    for k in range(2, l+1):
        if i % k == 0:
            stuff = True
    if stuff == False:
        primes.add(i)
    stuff = False

print(f"{len(primes)} primes in the list")