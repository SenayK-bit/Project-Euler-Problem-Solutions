import time

startTime = time.perf_counter()

fibonacciNumbers = [1, 2]
sum = 0

while True:
    nextNumber = fibonacciNumbers[-1]+fibonacciNumbers[-2]
    if nextNumber < 4000000:
        fibonacciNumbers.append(nextNumber)
    else:
        break

for i in fibonacciNumbers:
    if i%2 == 0:
        sum += i

print(f"{sum} is the sum of all even fibonacci numbers less than 4,000,000.")

endTime = time.perf_counter()
programRunTime = endTime - startTime

print(f"Program ran for {programRunTime} seconds")