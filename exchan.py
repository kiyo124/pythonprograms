'''try:
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    print(a/b)
except ZeroDivisionError:
    print("division by zero")
finally:
    print("Goodbye")'''

#task 1
try:
    print("Reading File Content\n")
    file=open('sample1.txt','r')
    print('Line 1:',file.readline())
    print('Line 2:',file.readline())
    file.close()
except :
    print('The given file does not exist ')

#task 2
