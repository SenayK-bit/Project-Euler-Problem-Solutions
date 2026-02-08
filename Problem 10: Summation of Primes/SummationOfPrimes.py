import time

startTime = time.perf_counter()

limit = 2000000
sumOfPrimes = 0

is_prime = [True] * (limit+1) #Adding 1 to the limit to create an extra marker for 0
is_prime[0] = is_prime[1] = False #Setting 0 and 1 to False, meaning they aren't primes.

for i in range(2, limit+1):
    if is_prime[i]:
        for p in range(i*i, limit+1, i): #Starts with i*i because 2i would have been labelled not prime when i = 2. Same thing with 3i and this goes on until i * i.
            is_prime[p] = False

for x in range(limit+1):
    if is_prime[x]:
        sumOfPrimes += x

print(sumOfPrimes)

endtime = time.perf_counter()
programRunTime = endtime - startTime
print(f"Program ran for {programRunTime} seconds.")