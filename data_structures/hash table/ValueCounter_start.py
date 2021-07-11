# using a hashtable to count individual items


# define a set of items that we want to count
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a hashtable object to hold the items and counts
# counter = dict()  # use below
counter = {}  

# TODO: iterate over each item and increment the count for each one
for item in items:
    if item in counter.keys():
        counter[item] +=1
    else:
        counter[item] = 1

# print the results
print(counter)
''' {'apple': 5, 'pear': 3, 'orange': 4, 'banana': 2, 'kiwi': 1} '''


"""
Example #2
"""
word = "mississippi"
counter = {}
for letter in word:
    counter[letter] = counter.get(letter, 0) + 1
print(counter)
''' {'m': 1, 'i': 4, 's': 4, 'p': 2} '''

"""
Example #3
"""
from collections import defaultdict

word = "mississippi"
counter = defaultdict(int)    #  int() as a default factory function
for letter in word:
    counter[letter] = counter.get(letter, 0) + 1
print(counter)
''' defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2}) '''