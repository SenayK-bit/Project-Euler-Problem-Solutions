## Problem 3: Largest Prime Factor

The problem asks for the largest prime factor of 600851475143. To solve this problem, the solution divides the number by all of its factors until the quotient is 1. Once the quotient is 1, the last divisor would be the greatest prime factor since all other factors would have been removed (meaning our largest prime factor doesn't have a factor, proving its prime) and because the original number was divided by its smallest factor first, going up to its largest factor, proving that the last factor is the largest. You can think of it almost like a filter, where all the factors of the number in question are filtered out (by dividing the number by that factor), leaving us with the largest prime factor.

Run Time = 0.0005 seconds