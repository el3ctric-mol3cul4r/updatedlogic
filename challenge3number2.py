def check(num):
    if num % 2 == 0:
        print("Even")
    if num % 2 != 0:
        print("Odd")

x = int(input("Type a number"))
check(x)
