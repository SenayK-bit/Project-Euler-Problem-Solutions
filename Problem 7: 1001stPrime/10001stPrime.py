import time

startTime = time.perf_counter()

primes = [2, 3]
number = 4
isPrime = True

while True:
    squareRoot = (number ** 0.5)
    for p in primes:
        if p > squareRoot:
            break
        if p < squareRoot or p == squareRoot:
            if number % p == 0:
                isPrime = False
                break
    if isPrime:
        primes.append(number)
    number += 1
    if len(primes) == 10001:
        break
    isPrime = True

print(f"The 10,001st prime is {primes[-1]}")

endTime = time.perf_counter()
programRunTime = endTime - startTime
print(f"The program ran for {programRunTime} seconds.")