# Demonstrate how to use Python's list comprehension syntax to produce the 
# list [1, 2, 4, 8, 16, 32, 64, 128, 256].

new_list = [2**n for n in range(0, 9)]
print(new_list)