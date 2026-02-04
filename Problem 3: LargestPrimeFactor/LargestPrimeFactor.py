import time

startTime = time.perf_counter()

bigNumber = 600851475143
divisor = 2

while (bigNumber != 1):
    if bigNumber % divisor:
        divisor += 1
    else:
        bigNumber //= divisor

print(f"{divisor} is the biggest prime factor of 600851475143")

endTime = time.perf_counter()
programRunTime = endTime - startTime
print(f"Program ran for {programRunTime}")