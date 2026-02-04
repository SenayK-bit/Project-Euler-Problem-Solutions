## Problem 2: Even Fibonacci Numbers

This problem asks for the sum of all even fibonacci numbers less than 4000000. Note that a fibonacci number is a number that appears in the sequence: 1, 2, 3, 5, 8, 13, 21... where each number after 2 is the sum of the two previous numbers. To solve this problem, one first needs to find all the fibonacci numbers that are less than 4000000, and then pick out all the even numbers and sum them up. And that's pretty much what the algorithm does. This method uses brute force but is nevertheless an efficient solution as the fibonacci numbers scale up quickly. Case in point, there are only 33 fibonacci numbers that are less than 4000000.

Run Time = 30 microseconds.