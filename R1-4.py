# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sum_of_sqrs(k):
    if k >= 0:
        sqr_sum = 0
        while k > 0:
            count = k - 1
            count *= count
            sqr_sum += count
            k -= 1
        return sqr_sum
    else:
        return False

print("The sum of n-1 squares for integer -1 is: ", sum_of_sqrs(-1))
print("The sum of n-1 squares for integer 5 is: ", sum_of_sqrs(5))
print("The sum of n-1 squares for integer 10 is: ", sum_of_sqrs(10))
print("The sum of n-1 squares for integer 20 is: ", sum_of_sqrs(20))