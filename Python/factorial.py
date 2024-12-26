'Write a program to calculate the factorial of a given number'
def fact(n):
    if(n==0):
        return 1
    else:
        return  n*fact(n-1)
a=int(input("Enter the number:"))
print("The factorial is:",fact(a))
