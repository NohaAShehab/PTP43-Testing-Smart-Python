

course = 'pyhon'  # variable with global scope


# ###### this variable can be accessed anywhere in the script ?
# print(course)

""" print global scope variable from inside function """

# def sayhello():
#     print("== hello world===")
#     print(f"course = {course}")  # Operation successfully run
#
# sayhello()



# def modifycourse():
#     # any variable defined inside a function --> has scope ((local scope ))
#     course = input("please enter course name: ") # this create new local variable in this scope
#     print(f"course = {course}")
#
# modifycourse()
# print(f"after calling the function course ={course}")


"""modify global variable define in the script from inside the function  """

#
# def modifycourse():
#     global course ## use the global course variable , and please don't create new one
#     course = input("please enter course name: ")
#     print(f"course = {course}")
#
# modifycourse()
# print(f"after calling the function course ={course}")
#



############################################

""" python support function in side a function """


# def outerfunction():
#     print("---> hello from outer function ")
#     name = input("please enter your name ") # local scope variable
#     # can be accessed anywhere in any inner function
#     def greetuser():
#         print(f"nice to you {name}")
#
#     greetuser()
#
# outerfunction()

""" modify local variable from inside inner function """
# def outerfunction():
#     print("---> hello from outer function ")
#     name = 'Ahmed' # local scope variable
#     # can be accessed anywhere in any inner function
#     def modifyname():
#         name = input("please enter you fullname")  # create new local variable inside
#         # the modify function scope
#         print(f"name modified to {name}")
#     modifyname()
#     print(name)


def outerfunction():

    print("---> hello from outer function ")
    name = 'Ahmed' # local scope variable
    def modifyname():
        nonlocal  name  # please don't create new local variable
        # use the variable of your parent
        name = input("please enter you fullname")
        # the modify function scope
        print(f"name modified to {name}")
    def formatname():
        nonlocal name
        name= f"{{{name.upper()}}}"
    choice = input("please enter m for modify , f for format , a for all: ")
    if choice=='m':
        modifyname()
    elif choice=='f':
        formatname()
    elif choice=='a':
        modifyname()
        formatname()
    else:
        print("--- please enter correct option")



    print(name)



outerfunction()

##################### match case #############
command = 'Hello, World!'
match command:
    case 'Hello, World!':
        print('Hello to you too!')
    case 'Goodbye, World!':
        print('See you later')
    case other:
        print('No match found')


























