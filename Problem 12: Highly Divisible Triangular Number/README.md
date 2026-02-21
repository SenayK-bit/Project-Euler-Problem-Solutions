## Problem 12: Highly Divisible Triangular Number

The problem asks for the first triangular number with over 500 divisors. 

To solve this problem, the algorithm generates triangular numbers and then checks their prime factors. These prime factors are taken from a list that is continually updated with primes up to a limit, which is the square root of the triangular number.

Once all the prime factors (up to the limit) that divide the triangular number have been found, we determine all possible factors that can be formed from them. To do this, we note that for any specific prime factor that divides the triangular number n times, it can do one of the following to any given factor: divide it zero times, divide it once, divide it twice, and so on up to n times. There will therefore be n + 1 possible outcomes for a prime that divides the triangular number n times. To find the total number of combinations (i.e., factors), we multiply the number of outcomes for each prime. That is, if a triangular number x has prime factors 2, 3, and 5, which divide x 3, 2, and 1 times respectively, then there are (3 + 1) × (2 + 1) × (1 + 1) possible factors of x.

If a given triangular number does not have more than 500 factors, the algorithm moves on to the next triangular number and repeats, stopping only once a triangular number with more than 500 factors is found.