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

    2- do operation
        read
        write
    3- close file ::
        ===> save content
"""

""" open file for writing """

try:
    fileobject = open("mycv.txt", 'w')
except Exception as e:
    print(e)
    exit()
else:
    print(fileobject)  # file object
    # fileobject.write("=====> Good morning Testing <=======\n")
    # fileobject.write("===> Good morning Mohamed Tarek <===")
    data = ['ahmed\n', 'Mohamed\n', 'amany\n', 'ali\n', 'Omar\n']
    fileobject.writelines(data)  # iterable --> must be string

    fileobject.seek(15)  # starting from the beginning of the file
    fileobject.write("----- The lecture is very boring -----")


    fileobject.close()














