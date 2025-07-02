# define function
# return
print("passing argument to a function")
def sum(a,b):
    return a+b
x=int(input("enter first number"))
y=int(input("enter second number"))
ans=sum(x,y) # passing argument to a function
print(ans)

#passing function as a arguments
print("pasing argument as a function ")
def add1(a,b):
    return a+b
c=add1(x,y)
def square(d):
    print("after adding number is",d)
    print("square of ",d," is :",c**2)
square(c)
