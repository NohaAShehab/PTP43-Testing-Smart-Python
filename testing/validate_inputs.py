print("""-----welcome to validate inputs module ----------"
      "this line will be called automatically when you just import the module, part of it  """)

def validateInputNumber(message):
    num = input(message)
    if num.isdigit():
        num= int(num)
        print(num, type(num))
        return int(num)
