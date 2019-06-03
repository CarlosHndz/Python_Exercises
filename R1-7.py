# Give a single command that computes the sum from Exercise R1-6, relying
# on Python's comprehension syntax and the built-in sum function.

number = 100
total = sum(k*k for k in range(1, number, 2))

print("The sum of all odd positive integers less than ", number, " equals: ", total)