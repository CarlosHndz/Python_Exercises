# Write a short Python function that takes a sequence of integer values and 
# determines if there is a distinct pair of numbers in the sequence whose 
# product is odd.

def odd_product(data):
    count = 0
    length = len(data)

    for x in range(0, length-1):
        for y in range(x+1, length):
            #print("x = ", data[x], ", y = ", data[y])
            product = data[x] * data[y]
            if product % 2 == 1:
                count += 1
                #print("x = ", data[x], ", y = ", data[y], ", product = ", product)
    return count

A_list = [1, 2, 3, 4, 5, 6]
print("The number of pairs in the sequence whose product is odd equals: ", odd_product(A_list))