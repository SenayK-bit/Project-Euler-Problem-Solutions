bigNumber = 600851475143
divisor = 2

while (bigNumber != 1):
    #This checks all numbers greater than 2 for one that fully divides our number. It checks a new divisor if the older one doesn't work.
    if bigNumber % divisor:
        divisor += 1
    #When a divisor is found, it divides our number repeatedly and updates it to the new value until it can no longer fully divide the new value of our number.
    else:
        bigNumber //= divisor
    #Once our number gets to 1, the most recent value for the divisor would be the largest prime factor

print(f"{divisor} is the biggest prime factor of 600851475143")