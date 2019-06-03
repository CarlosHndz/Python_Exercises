# What parameters should be sent to the range constructor, to produce a range
# with values 50, 60, 70, 80?

# range has a start, stop, and step elements so the answer would be the following
# range(50, 90, 10)
# The stop element is not inclusive, so the range would be 50, 60, 70, and 80
# not including 90.

for k in range(50, 90, 10):
    print(k)
