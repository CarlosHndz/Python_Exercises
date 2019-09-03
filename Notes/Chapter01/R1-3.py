# Write a short Python function, minmax(data), that takes a sequence of one
# or more numbers, and returns the smallest and largest numbers, in teh form
# of a tuple of length two. Do not use the built-in function min or max in 
# implementing your solution

def minmax(data):
    min = 0
    max = 0
     
    for j in range(len(data)):
        if data[j] == data[min]:
            max = j
            min = j

        elif data[j] < data[min]:
            min = j

        elif data[j] > data[max]:
            max = j
            
    print("The min number is: ", data[min])
    print("The max number is: ", data[max])
        

numList = (1, 2, 3, 4, 5, 0, -1, -10)
minmax(numList)