totalProducts = set()
palindromes = []

#First, we figure out all the unique numbers that are products of two three digit numbers. 
for i in range(100, 1000):
    for k in range(100, 1000):
        #Since 'totalProducts' is a set, it will only store unique values.
        totalProducts.add(i*k)

for l in totalProducts:
    #This part looks for palindromes in the set that contains the products of two, three digit numbers.
    if str(l) == str(l)[::-1]:
        #All such palindromes are added to the list 'palindromes'
        palindromes.append(l)

largestPalindrome = 1
for p in palindromes:
    #Here, we check all the palindromes in the list 'palindromes'. If one of them are bigger than our current value for 'largestPalindrome', then we update it to the new largest palindrome.
    #After looking through all the palindromes, the largest of them will be stored in 'largestPalindrome'
    if p > largestPalindrome:
        largestPalindrome = p

print(f"The largest palindrome is {largestPalindrome}")