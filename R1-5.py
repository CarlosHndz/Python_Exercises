# Give a single command that conputes the sum of Exercise R1-4, relying on 
# Python's comprehension syntax and the built-in sum function.

total = sum(k*k for k in range(1, 20))
print(total)
