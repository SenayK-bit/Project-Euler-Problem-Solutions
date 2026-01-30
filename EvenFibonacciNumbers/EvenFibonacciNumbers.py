fibonacciNumbers = [1, 2]
sum = 0


while True:
    #This checks to see if the the next fibonacci number is less than 4000000, and if it isn't, it adds that number to the list 'fibonacciNumbers'
    if fibonacciNumbers[-1]+fibonacciNumbers[-2] < 4000000:
        fibonacciNumbers.append(fibonacciNumbers[-1]+fibonacciNumbers[-2])
    #Should the next fibonacci number be less than 4000000, the loop is broken and we are left with a list of fibonacci numbers below 4 million.
    else:
        break

for i in fibonacciNumbers:
    #The last step involves checking every number in our fibonacci sequence and counting up how many of which are even.
    if i%2 == 0:
        sum += i

print(f"{sum} is the sum of all even fibonacci numbers less than 4,000,000.")