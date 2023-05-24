""" --> based sequence ? --->"""


""" list mutable datatype can hold different values from different datatypes"""
"""1- define a list """
l = []  # empty
myl = list()  # another way of definition
print(l)

l = ['Amany', 'Ahmed', 'ITI', True, 44.5, 44, 'iti', 'iti', 'ITI']
print(l)

"""2- access elements using index """
print(l[3])

"3- list is mutable -=-->modify element at existing index "
l[3]='Python'
print(l)
# l[100] = 'test' #list assignment index out of range
# l[6] = 'iti'
"4- append element to the list "
l.append('appeneded_element')
print(l)
"5- insert element to the list ===> at certain posistion ? --> index"
# l.insert(4, 'inserted')
# print(l)
# l.insert(100, 'another inserted')
# print(l)

"6- pop elements from the list ?"
# popped_element = l.pop()  # return with the last element in the list
# print(l)
# popped_element = l.pop(0)  # return with the last element in the list
# print(l)

"""7-remove element from the list """
l.remove('iti') # remove first occurence of the element
print(l)

"""8- list concat"""
l1 = [33,5,66]
l2 = [434,65,6, 'iti']
l3 = l1  + l2 ## new variable
print(l3)

"""9- extend a list"""
l1.extend(l2)
print(l1)

"""10- sort list ---> depends on the comparision ---> compare between items from the same type"""

names = ['Ahmed', 'Ali', 'Amany', 'Noha', 'Mohamed', 'Mahmoud']

# names.sort()  # ascending
# print(names)

names.sort(reverse=True)
print(names)
"""11-reverse a list"""

myl = ['iti', 'ahmed', 33, 344.4, False, True, 'abc']
myl.reverse()
print(myl)


"""12- looping over the list ---> """

# for item in myl:
#     print(f"item = {item}")


"13- print index , element in the list ?"
# count = 0
# for item in myl:
#     print(f"index = {count}, item = {item}")
#     count +=1


""" enumarate function ? """
# print(enumerate(myl))
# ll= list(enumerate(myl))
# print(ll)
# for abbass, fernas in enumerate(myl):
#     print(f'index={abbass}, element = {fernas}')

## range function--> generate iterable object can be used to generate number

# r = range(10) # return with iterable object --> from 0 , to 9
# print(r)  # 0, 10
# l = list(r)
# print(l)

# myr = range(1,20)  # start 1 , end 20
# print(list(myr))

# myr = range(1,20, 2)  # start 1 , end 20
# print(list(myr))

r= range(10)
print(r)

l= list(r)
""" 
    for element in iterable:
        print(element)
"""

for abbass in r:
    print(abbass)

####################

ll = [23,True, 'ahmed', ['python', 'selenium', 'linux'], False ]

print(ll[3][1])

""" min , max ---> list elements must be from the same type """
l  =[4,3,5,6]
print(min(l))

ll=[[40,5], [40,5,7]]
print(min(ll))

""" in operator ? ---> retrun True if elements exists in the list  """

names = ['ahmed', 'ali', 'test']
print('ahmed' in names)


# noha --> nh
# iti 0 2
4
[[1], [2,4],[3,6,9], [4,8,12,16]]