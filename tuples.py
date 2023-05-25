""" tuple , lists -> elements are ordering in memory according how you add them """
""" --> based sequence ? --->"""
#
#
""" tuple immutable datatype can hold different values from different datatypes"""
"""1- define a tuple """
t = ()  # empty
myt = tuple()  # another way of definition
print(t)
#
t = ('Amany', 'Ahmed', 'ITI',[True, 44.5, 44], 'iti', 'iti', 'ITI')
# print(t)
"count element occurrence"
print(t.count('iti'))
#
"""2- access elements using index """
# print(t[3].append('noha'))
# print(t)
#
"3- tuple is immutable -=--> cannot modify element at existing index "
# t[3]='Python' #'tuple' object does not support item assignment
# print(t)



#


#
"""5- tuple concat"""
t1 = (33,5,66)
t2 = (434,65,6, 'iti')
t3 = t1  + t2 ## new variable
print(t3)
#

# """5- looping over the tuple ---> """
#
for item in t:
    print(f"item = {item}")


"13- print index , element in the tuple ?"
# count = 0
# for item in t:
#     print(f"index = {count}, item = {item}")
#     count +=1


""" enumarate function ? """
# tt= tuple(enumerate(t))
# print(tt)
for abbass, fernas in enumerate(t):
    print(f'index={abbass}, element = {fernas}')
#
# ## range function--> generate iterable object can be used to generate number
#
r = range(10) # return with iterable object --> from 0 , to 9
# # print(r)  # 0, 10
t = tuple(r)
print(t)

numbers =tuple( range(4,100))
print(numbers)


#
""" min , max ---> tuple elements must be from the same type """
t  =(4,3,5,6)
print(min(t))
#

""" in operator ? ---> retrun True if elements exists in the tuple  """
#
names = ('ahmed', 'ali', 'test')
print('ahmed' in names)


""" tuple of one item """
# names = ('Amany',)
# # names = tuple(['Amany'])
# print(type(names))

""" cast list to tuple ? """
l = ['iti',33,True, ['a','b', 'c']]
t = tuple(l)
print(t)

l = list(t)
print(l)


print(tuple('noha'))

print('a' in 'noha')