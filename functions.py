
"""
    public void function hello(){

    }
    # special variable ---> refers to behaviour
"""
# def sayhello():
#     pass
#
#
# print(type(print))
# print(type(sayhello))

""" function that do something """


# def sayhello():
#     print("----hello world----")
#
# "to call function"
# sayhello()
#
# """ what is the return of this function """
#
# res = sayhello()
# print(res)  # None

""

# def sayhello():
#     print("----hello world----")
#     return
#
# """ what is the return of this function """
# res = sayhello()
# print(res)  # None

############# function accept arguments , return result

# def sumnum(num1, num2):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(f'result = {res}')
#     return res
#
# numberss = sumnum(33,33)
# print(numberss)

############################
""" python is loosely dynamically typed lang. """

# def sumnum(num1, num2):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(f'result = {res}')
#     return res
#
# # numberss = sumnum("33","444")
# # print(numberss)
#
# numberss = sumnum(10,"444")
# print(numberss)


""" 
    (int x , int y )
"""
#############################
#
# def sumnum(num1 :int, num2: int):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(f'result = {res}')
#     return res

# numberss = sumnum("33","444")
# print(numberss)

# numberss = sumnum(10,"444")
# print(numberss)
#
# ### manually check datatypes used as a parameter

# print(isinstance(10, str))


# def sumnum(num1 :int, num2: int): # descriptive code
#     print(f"num1={num1}, num2={num2}")
#     if isinstance(num1, int) and isinstance(num2, int):
#         res = num1 + num2
#         print(f'result = {res}')
#         return res
#     print("---num2, num1 must be int ")
#
#
# num = sumnum(10,20)
# print(num)
#
# numm = sumnum(3,'rr')
# print(numm)

################# overloading

# def sumnum(num1:int):
#     print(num1)
# def sumnum(msg:str, num2: int):
#     print(msg, num2)
#
#
# sumnum(10) # call function at line 107


### function with default arguments ?



#
# def sumnum(num1, num2=2):
#     if isinstance(num1, float):
#         pass
#     print(f'num1 = {num1}, num2 = {num2}')
#     print(num1, num2)
#
#
# sumnum(3,5)
# sumnum(10)

##################################################
"""===> function with variable of arguments <========"""

# print()
# print("Ahemd")
# print("Amany", 'Mohamed', True, 'abc')
"""
    public static void main (string [] args){
    }
"""

def askforstudents(*students):  # varaible number of arguments  ---> unknow
    print(students)



# askforstudents()
# askforstudents('Ahmed')
# askforstudents('Ahmed', 'mohamed', 'Ali')
#
# print(3,5,4, sep='|________|', end='}}{{')
# print("noha")

""" functions with keyword arguments """


def bio(**info):
    print(info)  # dict


bio(name='noha', age=31, work='iti')
bio(fname='amany')
bio()








