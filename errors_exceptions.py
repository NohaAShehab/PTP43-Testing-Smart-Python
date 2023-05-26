
"""
    runtime error

    logical errors

    syntax error ---> parser will guide to the fix the error
        --> when it happened the script will not start interpretation

"""

"logical error"

# def sumnum(num1, num2):
#     res = num1 + num2
#     print(res)
#     return res
#
# sumnum(2,2)
# # sumnum(3,4)

""" runtime errors """
#
#
# # print(name)  # runtime error
#
# # print(5/0) #ZeroDivisionError
#
#
# num = int(input("please enter number: "))
# print(num) #ValueError

""" handling exception ?"""


# try:
#     print(name)
# except:
#     print("==== problem happened =====")
#
# print("-------------------------------")

# try:
#     num = int(input("please enter number: "))
# except:
#     print("==== problem happened =====")
#
# print("-------------------------------")

""" """

# try:
#     print(name)
#     num = int(input("please enter number: "))
#
# except Exception as e :
#     print(f"==== problem happened ::: {e}=====")
#
# print("-------------------------------")


""" exception handling ---> fix issue ---> print error """
# try:
#     num = int(input("please enter number: "))
#
# except Exception as e :
#     num= 0
#     print(f"==== problem happened ::: {e}=====")
#     print("--- incorrect input, the application will close now")
#     exit(101)
#
# print("-------------------------------")
# print(num)


""" multiple excepts """

#
# try:
#     num = input("please enter num: ")
#     print(5/0)
#     print(name)
#
# except ValueError as ve :
#     print(f"{ve}, so num will be declared with 0")
#     num = 0
# except NameError as ne:
#     print(f"{ne}")
#     name = ''
# except Exception as e:
#     print(f"unknow input cause the application to stop please restart it ")
#     exit()

#
#
#
#############################


# try:
#     num = int(input("please enter num: "))
# except ValueError as ve :
#     print(f"{ve}, so num will be declared with 0")
# except Exception as e:
#     print(f"unknow input cause the application to stop please restart it ")
#     exit()
# else:
#     """ optional block """
#     "this block will be executed only if there is no problem"
#     print(num)
""" operation completed  """
# try:
#     num = int(input("please enter num: "))
# except ValueError as ve :
#     print(f"{ve}, so num will be declared with 0")
# except Exception as e:
#     print(f"unknow input cause the application to stop please restart it ")
#     exit()
# else:
#     """ optional block """
#     "this block will be executed only if there is no problem"
#     print(num)
# finally:
#     print("---- this block will be executed always---")
#



""" raising error """


# num = int(input("please enter num: "))


#
# def sumnums(num1, num2):
#     print(f"-- num1={num1}, num2 = {num2}")
#     if isinstance(num1, int) and isinstance(num2, int):
#         res = num1 + num2
#         return res
#
#     raise TypeError("Num1 and num2 should integers ")
#
# sumnums(3,4)
# sumnums('iti', 'test')



def askfornum(message):
    while True:
        num1 = input(message)
        if num1.isdigit():
            return int(num1)
        print("--- please enter valid number ")
def divnums():
    num1 = askfornum('please enter num1: ')
    num2 = askfornum('please enter num2: ')
    if num2==0:
        raise ZeroDivisionError("cannot divide by zero")
    print(f"num1={num1}, num2={num2}")
    res = num1/ num2
    print(res)

divnums()
























