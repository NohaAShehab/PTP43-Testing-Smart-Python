"""

    simple version files --> flat files (.txt)
    ===> binary image

    1- open file
        open(filename:str, mode)
        r ==? reading --> read whole the content of the file ==> from the beginning of the file >>
        w ==? writing --> write content to the file starting from the beginning of the file?
            --> erasing the old data
            ---> if file doesn't exist python will try to create it
        a ==? append --> open file for writing starting from the end file =keep old content=
        --> if file doesn't exist python will try to create it

    2- do operation
        read
        write
    3- close file ::
        ===> save content
"""
import time

""" open file for appending """

# try:
#     fileobject = open("mycv.txt", 'a')
# except Exception as e:
#     print(e)
#     exit()
# else:
#     # print(fileobject)  # file object
#     # fileobject.write("=====> Good morning Testing <=======\n")
#     # fileobject.write("===> Good morning Mohamed Tarek <===")
#     # data = ['ahmed\n', 'Mohamed\n', 'amany\n', 'ali\n', 'Omar\n']
#     # fileobject.writelines(data)  # iterable --> must be string
#
#     fileobject.seek(10000)  # starting from the beginning of the file
#     fileobject.write("----- The lecture is very boring -----")
#
#
#     fileobject.close()


###########################
def saveuser_to_file(userdata):
    try:
        fileobject = open("users.txt", 'a')
    except Exception as e:
        print(e)
        return False
    else:
        fileobject.write(userdata)
        fileobject.close()
        return True





def get_all_users():
    try:
        fileobject = open("users.txt", 'r')
    except Exception as e:
        print(e)
        return False
    else:
        users = fileobject.readlines()
        fileobject.close()
        return users


def generate_new_id():
    users = get_all_users()
    if users:
        # lastuser =users[-1]
        # print(lastuser)
        # lastuserdata= lastuser.strip('\n')
        # # print(lastuserdata)
        # lastuserdata =lastuserdata.split(':')
        # print(lastuserdata)
        # id = int(lastuserdata[-1])
        if users[-1].strip():
            id = int(users[-1].strip('\n').split(':')[-1])
        else:
            id = 0
        return id+1
    else:
        return 1


def check_unique_name(name):
    users = get_all_users()
    if users !=[]:
        for user in users:
            user_data = user.strip('\n').split(':')
            print(user_data[0], name)
            if name == user_data[0]:
                print(name == user_data[0])
                return False
        else:
            return True

    else:
        print("==== this is the first user =====")
        return True
def register():
    username = input("please enter username: ")
    res = check_unique_name(username)
    if not res:
        raise Exception("Duplicate name please try again")

    password= input("please enter password")
    # id = round(time.time())
    id = generate_new_id()
    userdata =f"{username}:{password}:{id}\n"
    saved = saveuser_to_file(userdata)
    print(saved)

register()



# import  time
# print(round(time.time()))

### delete data from the file ?
"""

    1- load file data into one LIST 
    2- MODIFY/ DELETE ELELMENT IN THE LIST 
    3- WRITE THE LIST AGAIN TO THE FILE 
"""

