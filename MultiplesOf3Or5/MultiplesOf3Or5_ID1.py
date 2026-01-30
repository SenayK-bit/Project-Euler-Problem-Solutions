sum = 0

for i in range(1000):
    ##This checks every number between 1 and 999 inclusive, and adds 1 to the variable 'sum' whenever it comes across a multiple of 3 or 5.
    if (i % 3) == 0 or (i % 5) == 0:
        sum += i

print(f"{sum} is the total of all multiples of 5 or 3 that are less than 1000.")