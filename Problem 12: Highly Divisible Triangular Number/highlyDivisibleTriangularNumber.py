import time

startTime = time.perf_counter()

triangularNumber = 10
nextNumber = 5
primeNumbers = [2, 3]
lastLimit = 3
is_prime = True

while True:
    numberOfFactors = 1
    triangularNumber += nextNumber
    nextNumber += 1
    for i in range(lastLimit, int(triangularNumber**0.5)+1):
        for k in primeNumbers:
            if k*k > i:
                break
            if i % k == 0:
                is_prime = False
                break
        if is_prime:
            primeNumbers.append(i)
        else:
            is_prime = True
    lastLimit = int(triangularNumber**0.5)
    copy = triangularNumber
    for i in primeNumbers:
        numberOfPrimeFactors = 1
        while (copy % i == 0):
            copy //= i
            numberOfPrimeFactors += 1
        numberOfFactors *= numberOfPrimeFactors
    if copy != 1:
        numberOfFactors *= 2
    if numberOfFactors > 500:
        print(f"{triangularNumber} is the first triangular number to have over 5 hundred divisors.")
        break

endTime = time.perf_counter()
runTime = endTime - startTime
print(f"Program ran for {runTime}seconds.")