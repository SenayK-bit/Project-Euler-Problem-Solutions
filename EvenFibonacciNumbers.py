fibonacciNumbers = [1, 2]
sum = 0

while True:
    if fibonacciNumbers[-1]+fibonacciNumbers[-2] < 4000000:
        fibonacciNumbers.append(fibonacciNumbers[-1]+fibonacciNumbers[-2])
    else:
        break

for i in fibonacciNumbers:
    if i%2 == 0:
        sum += i

print(sum)