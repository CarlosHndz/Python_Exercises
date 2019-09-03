# Write a short Python function, is_even(k), that takes an interger value
# and returns True if k is even, and False otherwise. However, your 
# function cannot use the multiplication, modulo, or division operators.

def is_even(k):
    while k > 0:
        k -= 2
        if k == 0:
            return True
    
    return False
        
def is_even_bitwise(m):
    
    if m & 1 == 1:
        return False
    else:
        return True
    

print("Is the number 1 even? ", is_even(1))
print("Is the number 2 even? ", is_even(2))
print("Is the number 44 even? ", is_even(44))
print("Is the number 79 even? ", is_even(79))

print("")

print("Is the number 1 even? ", is_even_bitwise(1))
print("Is the number 2 even? ", is_even_bitwise(2))
print("Is the number 44 even? ", is_even_bitwise(44))
print("Is the number 79 even? ", is_even_bitwise(79))