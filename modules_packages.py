"""
    modules , packages

    module --> any .py file is considered to be module
"""

"## import all the module --> import function"

# import  greetingmodule
#
# greetingmodule.sayhello('Ahmed')
#
# greetingmodule.sayWelcome('kljsdf')
import  greetingmodule as gt
gt.sayhello('Ahmed')
#####################################
'import part of the module ? '
# from greetingmodule import  sayWelcome
# sayWelcome('Ahmed')
#


""" 
    folder--> python package 

"""
""" import module from package """

# import  testing.validate_inputs
#
# testing.validate_inputs.validateInputNumber('please enter age ')


"alias the import name ?"
# import  testing.validate_inputs as test
#
# test.validateInputNumber('please enter age ')



""" import part of the module from package """
# from testing.validate_inputs import validateInputNumber
# validateInputNumber('abc')
# from testing.validate_inputs import validateInputNumber  as vn
# vn('abc')





# import iti
#
# iti.describe_package()

""" check this """
# import  testing.validate_inputs


from testing.validate_inputs import validateInputNumber


#####################3
# from iti.students import askforstudents
#
# askforstudents(2)

from iti import askforstudents, validateInputNumber
askforstudents(3)
validateInputNumber('enter age please: ')
