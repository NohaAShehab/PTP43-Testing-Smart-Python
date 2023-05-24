

" string ---> "

name= 'Ahmed'
"1- get len of string "
# print(len(name))
"2- access string parts using index start from 0  --> is treated like an array "
# print(name[2])
# print(name[2:])
# print(name[::])
# print(name[::-1])
"3- string is immutable datatype"
# name[2]='M'  #TypeError: 'str' object does not support item assignment

"4- count char in the string "
course = 'odoo'
print(course.count('o'))

"5- get index of char "
print(course.index('o')) # return index of first occurence of the char

"6- format string operations  ---> return new string "
name = 'amany ramadan Hegazy '
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())

"7- strip , replace string parts"

message = 'nice to you meet you testing track ooooooooo ^^'
print(message.replace('o', '@'))
print(message.replace('o', '@').upper())
print(message.replace('o', '@', 2))

"ask user to enter input"
# message = input("please leave your opinion: ")  # input --> always returns with string
# print(message, type(message))

# name = input("please enter your name: ")
# print(len(name))

# name=name.strip()  # strip while spaces , tabs from the beginning and the end of the string
# print(len(name))

# name=name.lstrip()  # strip while spaces , tabs from the beginning the string
# print(len(name))

# name=name.rstrip()  # strip while spaces , tabs from the end the string
# print(len(name))
name = '  @@@noha@gmail.com@@   '
# name= name.strip("@ m") ## strip given chars from the beginning and the end of the string
# print(name)
# print(name.strip('@ '))
# print(name)
"8- concat string ---> concat strings only "
# fname = input("please enter firstname: ")
# lname = input("please enter lastname: ")
# fullname= fname + lname
# print(fullname)
# work = input("please enter your work")
# bio = "my name is "+fullname + "I works at " + work
salary = 2000
"9- format string "
# temp  = "my name is {0}, I works at {1}, salary= {2}"
# print(temp.format(fullname,work, salary ))
# print(temp.format(work, fullname, salary ))
# format with keyword args
temp  = "my name is {username}, I works at {workname}, salary= {salaryvalue}"
# ## foramt string using keyword arguments
# print(temp.format(workname=work, username=fullname, salaryvalue=salary))
""" f-format string """

# fname = input("please enter firstname: ")
# lname = input("please enter lastname: ")
#
# fullname = f"{fname} {lname}"
# print(fullname)


""" string interpolation """
# fname = 'Noha '
# mid = 'Abdelhady '
# lname = 'Shehab'
# # fullname= fname + mid +mid + lname
# fullname = fname + mid*2 + lname
# print(fullname)

""" examine string content """

name = input("please enter name : ")
# name = int(name)
print("isdigit",name.isdigit())  # False ---> return True if the string consists only from digits 1->9
print("isalpha",name.isalpha()) # return True if the string consists only from alphas a-z
print("isspace  ", name.isspace())
print("",name.islower())
print(name.isupper())
print("isdigit",name.isnumeric())  # accept superscript number --> return True


############################## Numbers
# z = 4 + 5j # complex
# c = complex(4, 5)
# print(z, c)
#

# print(min(5,6,7,23))
# print(min('Ahmed', 'Aziz', 'Ahme'))




