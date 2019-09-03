# Write a Python function that takes a sequence of numbers and 
# determines if all the numbers are different from each other (that is, they
# are distinct).

def different_num(data):
    length = len(data)
    for x in range(0, length-1):
        for y in range(x+1, length):
            if data[x] == data[y]:
                return False
                
    return True

A_list = [1, 2, 3, 4, 5, 6]
B_list = [1, 2, 3, 4, 4, 5, 6]
print("Are all the numbers in the sequece different from each other? ", different_num(A_list))
print("Are all the numbers in the sequece different from each other? ", different_num(B_list))