#1. print all natural numbers from 1 to n while loop
'''
n=int(input("enter number:"))
print("natural numbers from 1 to ",n,"are:")
i=1
while(i<=n):
    print(i,end=" ")
    i+=1
'''

#2. natural numbers from 1 to n in reverse using while loop
'''
n=int(input("enter number:"))
print("natural numbers from 1 to ",n,"are:")
i=0
while(i<n):
    print(n-i,end=" ")
    i+=1
'''

#3. all alphabets from a to z using while loop
'''
ch=ord('a')
while(ch<=ord('z')):
    print(chr(ch),end=' ')
    ch+=1
'''

#4. print all even numbers between 1 to 100 use while loop
'''
i=1
print("The even numbers between 1 to 100 are:")
while(i<=100):
    if(i%2==0):
        print(i,end=' ')
    i+=1
'''

#5. print all odd numbers between 1 to 100
'''
i=1
print("The odd numbers between 1 to 100 are:")
while(i<=100):
    if(i%2!=0):
        print(i,end=' ')
    i+=1
'''

#6. sum of all natural numbers between 1 to n
'''
n=int(input("enter number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(f"sum is {sum}")
'''

#7. sum of all even numbers between 1 to n
'''
n=int(input("enter number:"))
sum=0
for i in range(1,n+1):
    if(i%2==0):
        print(i, end=' ')
        sum+=i
print(f" sum is {sum}")
'''

#8. sum of all odd numbers between 1 to n
'''
n=int(input("enter number:"))
sum=0
for i in range(1,n+1):
    if(i%2!=0):
        print(i,end=' ')
        sum+=i
print(f"sum is {sum}")
'''

#9. print multiplication table of any number
'''
n=int(input("enter the number of which table:"))
i=1
while(i<=10):
    print(n,"*",i,"=",n*i)
    i+=1
'''

#10. count no of digits in a number
'''
n=input("enter a number:")
count=0
if(n.isdigit()):
    for i in n:
        count+=1
    print("no of digits is",count)
else:
    print("enter valid number")
'''

#11. find first and last digit of a number
'''
n=int(input("enter number:"))
n=abs(n)
last=n%10
first=n
while(first>=10):
    first=first//10
print("last",last)
print("first digit",first)
'''

#12. sum of first and last digit of a number
'''
n=int(input("enter number:"))
n=abs(n)
last=n%10
first=n
while(first>=10):
    first=first//10
print("last",last)
print("first digit",first)
print("sum of first and last digit is",first+last)
'''

#13. swap first and last digits of number
'''
n=int(input("enter number:"))
num=str(n)
if(len(num)==1):
    print("swapped number:",num)
else:
    swap=num[-1]+num[1:-1]+num[0]
    swapnum=int(swap)
    print("swapped number is:",swapnum)
'''

#14. calculate sum of digits of a number
'''
n=int(input("enter number:"))
num=str(n)
sum=0
for i in num:
    sum+=int(i)
print("sum of digits is",sum)
'''

#15. calculate product of digits of a number
'''
n=int(input("enter number:"))
n=abs(n)
num=str(n)
prod=1
for i in num:
    prod*=int(i)
print("product of digits is",prod)
'''

#16. enter a number and print its reverse
'''
n=input("enter a number:")
if(n.isdigit()):
    print("reverse number is",n[: : -1])
else:
    print("enter valid number")
'''

#17. check number is palondrome or not
'''
n=int(input("enter number:"))
temp=n
rev=0
while(n>0):
    digit=n%10
    rev=(rev*10)+digit
    n=n//10
if(temp==rev):
    print("palindrome")
else:
    print("not palindrome")
'''
'''
num=input("enter number:")
if(num==num[::-1]):
    print("palindrome")
else:
    print("not palindrome")
'''

#18. find frequency of each digit in a given integer
'''
n=int(input("enter a number:"))
freq=[0]*10
n=abs(n)
while(n>0):
    digit=n%10
    freq[digit]+=1
    n=n//10
for i in range(10):
    if(freq[i]!=0):
        print(f"Digit {i} occurs {freq[i]} times")
'''

#19. enter a number and print it in words
'''
words=["zero","one","two","three","four","five","six","seven","eight","nine"]
n=int(input("enter number:"))
n=str(n)
for i in n:
    print(words[int(i)],end=' ')
'''

#20. print all ASCII characters with their values
'''
for i in range(256):
    print("The ASCII value of character", chr(i)," = ",i)
'''

#21. power of number using for loop
'''
base=int(input("enter base:"))
power=int(input("enter power:"))
result=1
for i in range(power):
    result*=base
print(result)
'''

#22. find all factors of a number
'''
n=int(input("enter number:"))
print("the factors are:")
for i in range(1,n+1):
    if((n%i)==0):
        print(i,end=' ')
'''

#23. calculate factorial of a number
'''
num=int(input("enter number:"))
result=1
while(num>0):
    result*=num
    num-=1
print("the factorial is :",result)
'''

#24. find HCF of two numbers
'''
a,b=map(int,input("enter two numbers:").split())
min=min(a,b)
for i in range(1,min+1):
    if((a%i==0) and (b%i==0)):
        largest=i
print("HCF of numbers is:",largest)
'''
# Euclidean approach
'''
a,b=map(int,input("enter two numbers:").split())
while(b!=0):
    remainder=a%b
    a=b
    b=remainder
print("hcf of two numbers is:",a)
'''

#25. find LCM of two numbers
'''
a,b=map(int,input("enter two numbers:").split())
max=max(a,b)
while(True):
    if((max%a==0) and (max%b==0)):
        print(max)
        break;
    max+=1
'''

#26. check number is prime number or not
'''
n=int(input("enter number:"))
if(n>1):
    for i in range(2,n):
        if((n%i)==0):
            print("not prime number")
            break
    else:
        print("prime number")
'''

#27. prime numbers between 1 to n
'''
n=int(input("enter number:"))
print("The prime numbers between the given range are:")
for i in range(2,n+1):
    for j in range(2,i):
        if((i%j)==0):
            break
    else:
        print(i,end=' ')
'''

#28. sum of all prime numbers between 1 to n
'''
n=int(input("enter number:"))
sum=0
print("The prime numbers between the given range are:")
for i in range(2,n+1):
    for j in range(2,i):
        if((i%j)==0):
            break
    else:
        print(i,end=' ')
        sum+=i
print(f"sum is {sum}")
'''

#29. find all prime factors of a number
'''
n=int(input("enter number:"))
print("Prime factors are:")
for i in range(2,n+1):
    while((n%i)==0):
        print(i,end='*')
        n=n//i
'''

#30. check number is Armstrong or not
# 153=1^3 + 5^3 + 3^3=153  153,370,371,407,1634
'''
n=int(input("enter number:"))
num=str(n)
digits=len(num)
sum=0
for digit in num:
    digit=int(digit)
    sum+=digit**digits

if(sum==n):
    print("Armstrong number")
else:
    print("Not Armstrong number")
'''

#31. all strong numbers between 1 to n
'''
n=int(input("enter number:"))
print("Armstrong numbers are:")
for i in range(n+1):
    num = str(i)
    digits = len(num)
    sum = 0
    for digit in num:
        digit=int(digit)
        sum+=digit**digits

    if(sum==i):
        print(i,end=" ")
'''

#32. check number is perfect number or not
#A number is called a perfect number if the sum of its proper divisors (excluding itself) is equal to the number.
# 6,28,496,8128
'''
n=int(input("enter a number:"))
sum=0
for i in range(1,n):
    if((n%i)==0):
        sum+=i
if(sum==n):
    print("perfect number")
else:
    print("not perfect number")
'''

#33. print all perfect numbers between 1 to n
'''
n=int(input("enter number:"))
print("Perfect numbers in given range are:")
for i in range(1,n+1):
    sum=0
    for j in range(1,i):
        if((i%j)==0):
            sum+=j
    if(sum==i):
        print(i,end=' ')
'''

#34. check number is strong number or not
#A strong number is a number in which the
# sum of the factorials of its digits is equal to the number itself.
'''
n=int(input("enter number:"))
num=str(n)
sum=0
for i in num:
    result=1
    digit=int(i)
    while(digit>0):
        result*=digit
        digit-=1
    sum+=result

if(n==sum):
    print("strong number")
else:
    print("Not strong number")
'''

#35. all strong numbers between 1 to n
'''
n=int(input("enter number:"))
print("strong numbers in given range are:")

for i in range(1,n+1):
    temp=i
    sum=0
    while(temp>0):
        digit=temp%10
        result=1
        while(digit>0):
            result*=digit
            digit-=1
        sum+=result
        temp=temp//10

    if(i==sum):
        print(i,end=" ")
'''

#36. find fibinocci series upto n terms
'''
n=int(input("enter no of terms:"))
a,b=0,1
print("Fibinocci series using for loop:")
for i in range(n):
    print(a,end=' ')
    a,b=b,a+b
'''
'''
n=int(input("enter no of terms:"))
a,b=0,1
count=0
print("Fibinocci series using for loop:")
while(count<n):
    print(a,end=' ')
    a,b=b,a+b
    count+=1
'''

#37. find one's complement of binary number
'''
binary=input("enter binary number:")
comp=''
for bit in binary:
    if(bit=='0'):
        comp=comp+'1'
    elif(bit=='1'):
        comp=comp+'0'
    else:
        print("invalid binary number")
        exit()
print(f"one's complement of {binary} is {comp}")
'''

#38. find two's complement of binary number
'''
binary=input("enter binary number:")
comp=''
for bit in binary:
    if(bit=='0'):
        comp=comp+'1'
    elif(bit=='1'):
        comp=comp+'0'
    else:
        print("invalid binary number")
        exit()
two_comp=bin(int(comp,2)+1)[2:]
# to maintain same lengthoct
two_comp=two_comp.zfill(len(binary))
print(two_comp)
'''

#39. convert binary to octal number system-110101-65
'''
binary=input("enter binary number:")
dec=int(binary,2)
oct=oct(dec)[2:]
print("octal is ",oct)
'''

#40. binary to decimal
'''
binary=input("enter binary number:")
dec=0
power=len(binary)-1
for bit in binary:
    if(bit not in ('0','1')):
        print("enter valid binary number")
        exit()
    dec=dec+int(bit)*(2**power)
    power-=1
print("decimal number is:",dec)
'''

#41. octal to decimal-125-85
'''
octal=input("enter binary number:")
dec=0
power=len(octal)-1
for bit in octal:
    if(bit not in ('01234567')):
        print("invalid octal number")
        exit()
    dec+=int(bit)*(8**power)
    power-=1
print("decimal number is:",dec)
'''

#42. hexadecimal to decimal
'''
hex=input("enter hexadecimal number:")
dec=0
power=len(hex)-1
for bit in hex:
    if(bit not in ('0123456789ABCDEF')):
        print("invalid hex number")
        exit()
    if(bit.isdigit()):
        value=int(bit)
    else:
        value=ord(bit)-ord('A')+10
    dec+=value*(16**power)
    power-=1
print("decimal number is:",dec)
'''

#43. decimal to binary
'''
decimal=int(input("enter decimal number:"))
if(decimal==0):
    print("binary is 0")
else:
    binary=''
    while(decimal>0):
        remainder=decimal%2
        binary=str(remainder)+binary
        decimal=decimal//2
    print("binary is:",binary)
'''

#44. decimal to octal-83-123
'''
decimal=int(input("enter decimal number:"))
if(decimal==0):
    print("octal is 0")
else:
    octal=''
    while(decimal>0):
        remainder=decimal%8
        octal=str(remainder)+octal
        decimal=decimal//8
    print("binary is:",octal)
'''

#45. decimal to hexadecimal-254-FE
'''
decimal=int(input("enter decimal number:"))
hex_digits='0123456789ABCDEF'
if(decimal==0):
    print("hexadecimal is 0")
else:
    hex=''
    while(decimal>0):
        remainder=decimal%16
        hex=hex_digits[remainder]+hex
        decimal=decimal//16
    print("hexadecimal is:",hex)
'''

#46. binary to hexadecimal-11010111-D7
'''
binary=input("enter binary number:")
dec=int(binary,2)
hex=hex(dec)[2:].upper()
print("hexadecimal is ",hex)
'''

#47. octal to binary-57-101111
'''
octal=input("enter binary number:")
dec=int(octal,8)
binary=bin(dec)[2:]
print("octal is ",binary)
'''

#48. octal to hexadecimal-345-E5
'''
octal=input("enter octal number:")
dec=int(octal,8)
hexa=hex(dec)[2:].upper()
print("hexadecimal is ",hexa)
'''

#49. hexadecimal to binary---2F-101111
'''
hexa=input("enter hexadecimal number:")
dec=int(hexa,16)
binary=bin(dec)[2:]
print("binary is ",binary)
'''

#50. hexadecimal to octal---2F-57
'''
hexa=input("enter hexadecimal number:")
dec=int(hexa,16)
octal=oct(dec)[2:]
print("octal is ",octal)
'''
