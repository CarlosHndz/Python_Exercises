# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def sum_of_odd_squares(number):
    if number > 0:
        count = 0
        for k in range(1, number):
            if k % 2 == 1:
                count += (k * k)
        return count

print("The sum of odd positive integers smaller than 1: ", sum_of_odd_squares(1))
print("The sum of odd positive integers smaller than 10: ", sum_of_odd_squares(10))
print("The sum of odd positive integers smaller than 100: ", sum_of_odd_squares(100))
