# Python allows negative integers to be used as indices into a sequence, 
# such as a string. If string s has length n, and expression s[k] is used for 
# index -n <= k < 0, what is the equivalent index j >= 0 such that s[j] 
# references the same element?

'''
Python uses zero-indexing so seqences of length n have elements indexed 
from 0 to n-1 inclusive. However, when referencing to a specific element
in a sequece using a negative number, the last element in a sequence is
represented as -1. In this case the first element would be -n when using
negative indices. 

To answer the above question, the index j would need to be the value of index
k plus the lenght of the string (n) to match the same reference.
'''

