# Write a pseudo-code description of a function that reverses a list of n 
# integers, so that the numbers are listed in the opposite order than they were
# before, and compare this method to an equivalent Python function for doing
# the same thing.

'''
1. Get the length of the list and save the result to variable "length"
2. Set variable new_list equal to 0
3. Create a for loop to iterate from the index -1, which points to the last
   element in the list, to element -n, which should be the first element in
   the list using the range() function with -1 steps.
4. within the for loop append the current value associated with the current
   index to the "new_list" variable. 
5. Once the for loop is completed, return the variable "new_list", which
   should have the list elements in reverse order as the original list.
'''

'''
In comparison, the method reverse() modifies the sequence in plance which saves
space and does not create a separate copy of the list.
'''