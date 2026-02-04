import time

startTime = time.perf_counter()

numbers = []
factor = 2
smallestMultiple = 1

for i in range(1, 21):
    numbers.append(i)

while True:
    check = True 
    found_factor = False
    
    for k in range(len(numbers)):
        if numbers[k] % factor == 0:
            numbers[k] //= factor
            found_factor = True
            
        if numbers[k] > 1:
            check = False

    if found_factor:
        smallestMultiple *= factor
    else:
        factor += 1

    if check:
        break

print(f"The smallest multiple of all numbers between 1 and 20 inclusive is {smallestMultiple}.")

endTime = time.perf_counter()
programRunTime = endTime - startTime
print(f"The program ran for {programRunTime} seconds.")