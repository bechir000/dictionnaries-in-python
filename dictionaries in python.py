#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# empty dictionary
dict1 = {}

# dictionary using integer for keys
dict1 = {1: 'car', 2: 'bus'}

# dictionary using mixed keys
dict1 = {'color': 'yellow', 2: [3, 4, 5]}

# each item as a pair
dict1 = dict([(1,'car'), (2,'bus')])

# using dict()
dict1 = dict({1:'car', 2:'bus'})


# accessing elements
dict1 = {'color': 'red', 'score': 20}

# Output: red
print(dict1['color'])


# modifyingg Dictionary Elements
dict1 = {'color': 'blue', 'score': 12}

# update value
dict1['score'] = 18

# add item
dict1['color'] = 'green'




# create a dictionary
first_dict = {1: 10, 2: 5, 3: 8, 4: 111, 5: 12}

# remove a particular item, returns its value
print(first_dict.pop(4))

# remove all items
first_dict.clear()


