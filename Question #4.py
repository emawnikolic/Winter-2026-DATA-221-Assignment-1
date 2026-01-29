#%%
# Question 4 | Sorted Search with Conditions - Given a list of random values between 0 and 1 and a random value x:
# • Sort the list.
# • Find all indices where the list value is greater than or equal to x.
# • Print the sorted list, the value of x, and the first matching index (if one exists).
#%%
from random import random

values = [random() for i in range(20)]
x = random()

# your logic here