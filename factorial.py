a=int(input("enter number to find factorial:"))
def fact(b):
    if b<2:
        return 1
    else:
        return b*(fact(b-1))
fa=fact(a)
print("factorial of ",a," is: ",fa)