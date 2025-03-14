def palindrom(num):
    str_num=str(num)
    return str_num==(str_num[::-1])

num = int(input("Enter The number: "))
print(palindrom(num))
print("Hello")