'Write a program to check num is palindrome or not'
'''
n=int(input("Enter the number:"))
a=str(n)
b=a[: : -1]

if(n==int(b)):
    print("Palindrome")
else:
    print("Not a palindrome")
    '''
a=int(input("Enter the number:"))
temp=a
new=0
while(a>0):
    d=a%10
    new=new*10+d
    a=a//10
if(temp==new):
    print("Palindrome")
else:
    print("Not a palindrome")