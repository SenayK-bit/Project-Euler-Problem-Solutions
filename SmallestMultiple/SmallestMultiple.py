numbers = []
factor = 2
fullyFactored = 0
smallestMultiple = 1
check = 0

#This code generates all the numbers that we are intersted in. That is, the numbers between 1 and 20 inclusive.
for i in range(1, 21):
    numbers.append(i)

while True:
    #Here, we take note on whether a given divisor is a factor of atleast one number in our list.
    #If a divisor has its multiple(s) in our list, we update the multiple's value to the quotient between the divisor and the multiple.
    for k in range(20):
        if numbers[k] % factor:
            fullyFactored += 1
        else:
            numbers[k] //= factor
    #This piece of code tries to determine if the chosen divisor is a factor of any of the numbers in our list, changing the divisor if it isn't.
    #As such, all factors of the numbers in our list can be multiplied together, giving us the LCM.
    if fullyFactored != 20:
        smallestMultiple *= factor
    else:
        factor += 1
    fullyFactored = 0
    #Finally, we check to see if all our numbers have been fully divided and exit the loop when that's the case.
    for l in numbers:
        if l == 1:
            check += 1
    if check == 20:
        break
    check = 0

print(f"The largest multiple of all numbers between 1 and 20 inclusive is {smallestMultiple}.")