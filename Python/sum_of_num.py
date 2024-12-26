'Write a program that takes numbers as input and prints their sum'
n=int(input("Enter the no of numbers you want to sum :"))
sum=0
for i in range(n):
    a=int(input("Enter the %d number:"%(i+1)))
    sum=sum+a
print("The sum of numbers are :",sum)
