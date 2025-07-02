'''file1=open('sample1.txt','r')
print(file1.readline())
file1.close()'''
# 2nd way
with open("sample1.txt",'w') as file1:
    file1.write('Hello!\n')
    file1.close()


file1=open('sample1.txt','a')
print(file1.write('Welcome to the program'))

print("After appending")
print("after writing")
file1=open('sample1.txt','r')
print(file1.read())
file1.close()
#r+ for read and write mode
'''print("Reading File Content")
file = open('sample1.txt', 'r')
print('Line 1', file.readline())
print('Line 2', file.readline())'''

