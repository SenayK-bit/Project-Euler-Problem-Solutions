sumofSquares = 0
squareofSum = 0
sum = 0

#This solution first figures out the sum of squares and the square of the sum of numbers between 1 and 100 inclusive.
for i in range(101):
    sumofSquares += (i*i)

for i in range(101):
    sum += i
squareofSum = (sum*sum)

print(f"The difference between the square of the sum and the sum of the squares of numbers between 1 and 100 inclusive is {squareofSum-sumofSquares}")