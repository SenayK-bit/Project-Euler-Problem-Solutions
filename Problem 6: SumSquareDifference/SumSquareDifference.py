import time

startTime = time.perf_counter()

sumofSquares = 0
squareofSum = 0
sum = 0

for i in range(1, 101):
    sumofSquares += (i*i)
    sum += i
squareofSum = (sum*sum)

print(f"The difference between the square of the sum and the sum of the squares of numbers between 1 and 100 inclusive is {squareofSum-sumofSquares}")

endTime = time.perf_counter()
programRunTime = endTime - startTime
print(f"The program ran for {programRunTime} seconds")