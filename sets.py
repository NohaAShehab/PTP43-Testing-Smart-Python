

# #
# #
""" set mutable datatype can hold different values from different datatypes ---> hashable datatype
    -immutable-
    unsorted datatype

---"""
"""1- define a set """
mys = set()  # another way of definition
print(mys)
# # sets doesn't allow duplication
# mys = {'Amany', 'Ahmed', 'ITI', 'iti', 'iti', 'ITI',44,True}
# print(mys)
#

# mys = {'Amany', 'Ahmed', 'ITI', ['iti', 'iti'], 'ITI',44,True} #unhashable type: 'list'
mys = {'Amany', 'Ahmed', 'ITI', ('iti', 'iti'), 'ITI',44,True}
print(mys)

"3- set is mutable -=--> add / remove element from it "

mys.add('added_element') # added in random position
print(mys)

# popped_element = mys.pop()  # pop random element from the set
# print(popped_element)

mys.remove('ITI')
print(mys)

""" check element exists in set ? """

print("iti" in mys)

"""5- set concat"""
s1 = {33,5,66, 'iti'}
s2 = {434,65,6, 'iti', 'another element'}
# s3 = s1  + s2 ## new variable
# print(s3)
# s1.update(s2)
# print(s1)
s3=s1.union(s2)
print(s3)
# #
#
# """5- looping over the set ---> """
#
for item in mys:
    print(f"item = {item}")

#
"13- print index , element in the set ?"
for index, item  in enumerate(mys):
    print(f"{index}: {item}")


# """ min , max ---> set elements must be from the same type """
# t  ={4,3,5,6}
# print(min(t))
# #
#
### allow duplication --->
options = ['a', 'a', 'test','abc', 'data', 'data', 'test']
# unique_elements=[]
# for item in options:
#     if not(item in unique_elements):
#         unique_elements.append(item)
# print(unique_elements)
unique_elements = list(set(options))
print(unique_elements)