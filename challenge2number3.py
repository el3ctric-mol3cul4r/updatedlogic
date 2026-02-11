def fact(n):
    facto = 1
    for x in range(2, n+1): 
        facto *= x
    return facto
num = int(input("Input a number"))
print(fact(num))
#switch for x in range(1, n+1) facto *=x to n in range (1, x+1)
# or indent return in the loop 
# or forget to print