## Problem 10: Summation of Primes

The problem asks for the sum of primes up to 2,000,000. To solve this problem, this program uses the Sieve of Eratosthenes algorithm to generate primes. This algorithm is known to be fairly efficient one. It marks down numbers up to a specified limit as primes (except for 1 and 0) and then starting with the smallest prime (which would be 2), it finds all the multiples of that prime up to the limit and marks them as not primes, before doing the same thing for the second smallest prime (3). This problem is really efficient because it doesn't have to search a list (like the algorithm we used for problem 7: 10001st Prime) and instead relies on indexing, which is much more instant.

After marking all the primes from 1 to the limit, our program goes through all the numbers, summing up the primes. The final sum answers the problem.

Run Time = 0.4 seconds