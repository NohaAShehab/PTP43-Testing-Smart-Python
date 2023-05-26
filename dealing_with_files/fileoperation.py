"""

    simple version files --> flat files (.txt)
    ===> binary image

    1- open file
        open(filename:str, mode)
        r ==? reading --> read whole the content of the file ==> from the beginning of the file >>
        w ==? writing --> write content to the file starting from the beginning of the file?
            --> erasing the old data
        a ==? append --> open file for writing starting from the end file =keep old content=

    2- do operation
        read
        write
    3- close file ::
        ===> save content
"""

""" open file for reading """

try:
    fileobject = open("info.txt", 'r')
except Exception as e:
    print(e)
    exit()
else:
    print(fileobject)  # file object

    "### read file content into one string ?"
    # filedata=fileobject.read()
    # print(filedata)

    "read file content line by line"
    # lines = fileobject.readlines()
    # print(lines, type(lines))
    """ move file cursor to byte 10 """
    # fileobject.seek(10)
    # data = fileobject.read()
    # print(data)

    """ get users data """
    data = fileobject.readlines()
    users_login_credits = []
    for line in data:
        # print(line)
        user_data = line.strip('\n')
        user_data = user_data.split(":")
        print(user_data)
        users_login_credits.append((user_data[1], user_data[2]))
    fileobject.close()



def login():
    username = input("please enter username: ")
    password = input("please enter password: ")
    print(users_login_credits)
    login_credits = (username,password)
    if login_credits in users_login_credits:
        user_index = users_login_credits.index(login_credits)
        print(f"--- user logged in succesfully, {user_index}")
    else:
        print("no such user")


login()












