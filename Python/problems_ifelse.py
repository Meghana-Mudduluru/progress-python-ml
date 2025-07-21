#1. max between two numbers
'''
a,b=map(int,input("enter two numbers:").split())
if(a>b):
    print(a,"is greater than",b)
elif(b>a):
    print(b, "is greater than", a)
else:
    print("both are equal")
'''

#2. max between three numbers
'''
a,b,c=map(int,input("Enter three numbers:").split())
if((a>b) and (a>c)):
    print(a," is greater")
elif((b>a)and (b>c)):
    print(b,"is greater")
else:
    print(c,"is greater")
'''

#3. check num is neg,pos or zero
'''
a=int(input("enter a number:"))
if(a>0):
    print(f"{a} is positive number")
elif(a<0):
    print(f"{a}  is negative number")
else:
    print("It is zero")
'''

#4. check num is divisible by 5 and 11 or not
'''
num=int(input("Enter number:"))
if((num%5==0) and (num%11==0)):
    print(f"{num} is divisible by 5 and 11")
else:
    print("It is not divisible by both numbers")
'''

#5. check num is even or odd
'''
num=int(input("Enter number:"))
if(num%2==0):
    print("even")
else:
    print("odd")
'''

#6. check year is leap year or not
'''
num=int(input("Enter year:"))
if(((num%4==0) and (num%100!=0)) or num%400==0):
    print(f"{num} is leap year")
else:
    print(f"{num} is not a leap year")
'''

#7. check character is alphabet or not
'''
ch=input("Enter a character:")
if(ch.isalpha()):
    print("alphabet")
else:
    print("not alphabet")
'''

#8. take alphabet as input and check it is vowel or consonant
'''
ch=input("Enter a character:")
c=ch.lower()
if(c in {'a','e','i','o','u'}):
    print("it is vowel")
else:
    print("it is not an vowel")
'''

#9. take input any character and check it is alphabet/digit/spl character
'''
ch=input("Enter a character:")
if(ch.isalpha()):
    print(f"{ch} is alphabet")
elif(ch.isdigit()):
    print(f"{ch} is digit")
else:
    print(f"{ch} is spl character")
'''

#10. to check character is uppercase or lowercase alphabet
'''
ch=input("Enter character:")
if(ch.islower()):
    print("it is lowercase")
elif(ch.isupper()):
    print("it is uppercase")
else:
    print("not an alphabet")
'''

#11. input week numbers and print week day
'''
day=int(input("enter week number:"))
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
'''

#12. input month number and print no of days in the month
'''
month=int(input("enter month:"))
if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    print("31 days")
elif(month==4 or month==6 or month==9 or month==11):
    print("30 days")
elif(month==2):
    print("28 or 29 days")
else:
    print("enter valid month number")
'''

#13. count total notes in given amount
'''
amount=int(input("Enter amount:"))
note500=note100=note50=note20=note10=note5=note2=note1=0
if(amount>=500):
    note500=amount//500
    amount-=note500*500
if(amount>=100):
    note100=amount//100
    amount-=note100*100
if(amount>=50):
    note50=amount//50
    amount-=note50*50
if(amount>=20):
    note20=amount//20
    amount-=note20*20
if(amount>=10):
    note10=amount//10
    amount-=note10*10
if(amount>=5):
    note5=amount//5
    amount-=note5*5
if(amount>=2):
    note2=amount//2
    amount-=note2*2
if(amount>=1):
    note1=amount

print(f"amount is {note500} 500 notes {note100} 100 notes {note50} 50 notes {note20} 20 notes {note10} 10 notes {note5} 5 coins {note2} 2 coins and {note1} 1 coins")
'''

#14. input angles of triangle and check if it is valid or not
'''
a,b,c=map(int,input("enter angles of triangle:").split())
if((a+b+c==180) and a>0 and b>0 and c>0):
    print("valid triangle")
else:
    print("not a valid triangle")
'''

#15. enter sides of triangle and check valid or not
'''
a,b,c=map(int,input("enter sides of triangle:").split())
if((a+b)>c and (b+c)>a and (c+a)>b):
   print("valid triangle")
else:
    print("invalid triangle")
'''