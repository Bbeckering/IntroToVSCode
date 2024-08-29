# Problem #1
# What is missing in the while loop? 
# use a breakpoint in line 6 to debug
x =  1
while x < 10:
    print(x)
    x += 1
# Answer: Line 7, which adds 1 to the counter, was missing, creating an infinite loop
# problem #2
# use a breakpoint in line 14 to debug
mylist = list(range(5))

for x in range (1,5):
    print(f"Run No.:{mylist[x]}")
# Answer: The range in line 13 was set to 6 and because there is no 5th element in the list it created an Index error.