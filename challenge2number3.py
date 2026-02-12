def fact(n):
    facto = 1
    for x in range(2, n+1): 
        facto *= x
    return facto
num = int(input("Input a number"))
print(fact(num))