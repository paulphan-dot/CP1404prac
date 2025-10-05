import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# A random integer between 5 and 20,

# What was the smallest number you could have seen, what was the largest?
# Smallest: 5, largest: 20

# What did you see on line 2?
# A random odd integer chosen from the sequence 3, 5, 7, 9.

# What was the smallest number you could have seen, what was the largest?
# Smallest: 3, Largest: 9

# Could line 2 have produced a 4?
# No, because the step is 2, starting at 3, so it is the odd numbers. The possible values are 3, 5, 7, 9.

# What did you see on line 3?
# A random floating-point number between 2.5 and 5.5

# What was the smallest number you could have seen, what was the largest?
# Smallest: 2.5, Largest: 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))