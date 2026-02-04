import time

startTime = time.perf_counter()

sum = 0

for number in range(1000):
    if (number % 3) == 0 or (number % 5) == 0:
        sum += number

print(f"{sum} is the total of all multiples of 5 or 3 that are less than 1000.")

endTime = time.perf_counter()
programRunTime = endTime - startTime
print(f"Program ran for {programRunTime} seconds.")