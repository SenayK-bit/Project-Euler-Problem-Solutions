import time

startTime = time.perf_counter()

exit = False

for i in range(1, 1000):
    for p in range(1, 1000):
        c = (i**2+p**2)**0.5
        if (i + p + c) == 1000:
            a = i
            b = p
            exit = True
            break
    if exit:
        break
    

print(f"The product of the only pythagorean triplet which sums up to 1000 is {int(a*b*c)}.")

endTime = time.perf_counter()
programRunTime = endTime - startTime
print(f"The program ran for {programRunTime} seconds")