## Problem 5: Smallest Multiple

The problem asks to find the smallest multiple of numbers 1 - 20 inclusive. The question is essentially asking for the LCM of numbers 1 - 20, and so the algorithm looks for a factor and repeatedly divides and updates all the number in our list to the quotient, until it can't anymore, and then moves on to another factor. The product of all the factors used, each raised to the number of times they were used, would be the LCM.

Run Time = 91.75 microseconds