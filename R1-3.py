# Write a short Python function, minmax(data), that takes a sequence of one
# or more numbers, and returns the smallest and largest numbers, in teh form
# of a tuple of length two. Do not use the built-in function min or max in 
# implementing your solution

def minmax(data):
    min = 0
    max = 0
     
    for j in range(len(data)):
        print("Index: ", j, ", Value: ", data[j])
        if data[j] == data[min]:
            max = j
            min = j
            print("1-Max = ", max)
            print("1-Min = ", min)

        elif data[j] < data[min]:
            min = j
            print("2-Max = ", max)
            print("2-Min = ", min)

        elif data[j] > data[max]:
            max = j
            print("3-Max = ", max)
            print("3-Min = ", min)
            
    print("The min number is: ", data[min])
    print("The max number is: ", data[max])
        

numList = (1, 2, 3, 4, 5, 0, -1, -10)
minmax(numList)