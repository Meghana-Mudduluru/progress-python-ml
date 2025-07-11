'''
## addition of two numbers

#pre-defined variables

num1=30
num2=20
print("The sum of two numbers is",num1+num2)

# user input
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
print("The sum of two numbers is",n1+n2)

'''

'''
#sqrt of a number
import math
n1=int(input("Enter number:"))
print("sqrt of number is",math.sqrt(n1))
'''

# 2.enter two numbers and find thier sum
'''
a=int(input('enter number:'))
b=int(input('enter number:'))
print("the sum of number is:",a+b)
'''

# 3.all arithmetic operations of two numbers
'''
a=int(input('enter first number:'))
b=int(input('enter second number:'))
print("the sum is :",a+b)
print("the multiply is :",a*b)
print("the division is :",a/b)
print("the modulus is :",a%b)
print("the floor division is :",a//b)
print("the power is :",a**b)
'''

#4. 5. length and breadth and find perimeter of rectangle and also area
'''
from math import sqrt
l=int(input("enter length:"))
b=int(input("enter breadth:"))
print("perimeter of rectangle:",2*(l+b))
print("area of rectangle:",l*b)
print("diagonal of rectangle:",sqrt((l**2)+(b**2)))
print(3^4) # XOR operation
'''

#6. enter radius and find diameter,area and circumference
'''
from math import pi
r=int(input("enter radius:"))
print("diameter is:",2*r)
print("area is :",pi*r*r)
print("circumference is:",2*pi*r)
'''

#7.enter length in cm and convert into meter and km
'''
l=int(input("enter length in cm:"))
print("length in meters is:",l/100)
print("length in km is:",l/1000)
'''

#8. 9. celsius to fahrenheit and fahrenheit to celsius
'''
c=int(input("enter in celsus:"))
f=int(input("enter in fahrenheit:"))
f1=c*(9/5)+32
c2=(f-32)*(5/9)
print("in fahrenheit:",f1)
print("in celsius:",c2)
'''

#10. convert days into years ,weeks and days
'''
days=int(input("enter no of days:"))
years=days//365
weeks=(days%365)//7
days1=(days%365)%7
print(f"the {days} days is equal to : {years} years and {weeks} weeks and {days1} days .")
'''

#11. power of any number
'''
x=int(input("enter x:"))
y=int(input("enter y:"))
print(f"{x} power {y} is {x**y}.")
'''

#12. calculate sqrt

#13. find third angle in a triangle
'''
a=int(input("enter first angle:"))
b=int(input("enter second angle:"))
print("third angle is :",180-(a+b))
'''

#14. using base and height find area of triangle
'''
b=int(input("enter base:"))
h=int(input("enter height:"))
print("area of triangle is:",(b*h)/2)
'''

#15. area of equilateral triangle
'''
from math import sqrt
s=int(input("enter side of equilateral triangle:"))
print("area is:",(sqrt(3)*s*s)/4)
'''

#16. enter marks of 5 subjects and calculate total,avg and percentage
'''
a,b,c,d,e=map(int,input("enter marks of 5 subjects").split())# multiple input taking
total=a+b+c+d+e
avg=total/5
per=(total/500)*100
print(f"the total is {total}. avg is {avg} and the percentage is {per}.")
'''

#17. 18. enter P,T,R and calculate S.I and C.I
'''
p=int(input("enter p:"))
t=int(input("enter t:"))
r=int(input("enter r:"))
si=(p*t*r)/100
ci=p*((1+(r/100))**t)-p
print("S.I is:",si)
print("C.I is:",ci)
'''
