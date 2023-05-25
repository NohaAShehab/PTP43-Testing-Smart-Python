""" dictionary is mutable datatype"""
""" unlabeled data"""
info = ['noha', 31, 'iti', 'engineering', 'masters', 'phd', 'egypt']
print(info)

""" set--> provide unique elements ---> list ---> provide indexed elements
        0: 'iti'
        'abc' : 'iti
    dict ===> comma seperated key value pair --> 
    unique keys
"""
"""
    #unique keys --> 
    {
        key1:value, 
        key2, value
    }
"""
"1- define dict"
info = {
    "name":'noha',  "age":31, "work":'iti',
    "spec":'engineering', "highest_degree":'masters',
    "now":'phd', "lives_in":'egypt'}

myd = {}  # dict
d = dict()
#################################
# access elements using keys instead of index (tuple, list)
## no index in dictionary but keys
"""1- get len of the dict """
print(len(info))

""" access element using keys """
print(info['work'])
""" modify element using key """
info['work']='Information technology Institute'
print(info)

info["track"]='testing'
print(info)

""" check if element exists in the dict """
print('noha' in info) # in operator --> check if element exists in the keys

""" get keys , values of dict ?"""
# keys = info.keys()  # dict keys object --> can be casted to a list , loop over it
# print(keys)
## you can it to alist

# keys = list(keys)
# for k in info.keys():
#     print(k)
############
# values = info.values()  # dict keys object --> can be casted to a list , loop over it
# print(values)
#
# for v in values:
#     print(v)

# print('noha' in info.values())

## get keys, values ?

items = info.items()  #dict_items
print(items)
items = list(items)  # list of tuples
print(items)

# myd = {
#     "name":"Amany",
#     "nickname":"Amany",
#     "track":'testing'
# }
# print(myd.get("name"))
# print(myd['name'])

############# loop over the dict ?

name = input("please enter first name: ")
bio = f'my name is {name}'
print(bio)

for item in info:  # for in dict ---> item represent key ?
    print(f"{item}: {info[item]}")

######################################
""" update """

myinfo = {"city":"cairo",
          "name":"Noha Sehhab"}

print(info)
info.update(myinfo)
print(myinfo)
print(info)


# info.clear() # remove all the key value pairs
print(info)

# del variablename  # remove element from the memory