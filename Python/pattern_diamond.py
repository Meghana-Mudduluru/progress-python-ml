n=int(input("Enter no of rows :"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end='  ')
    for k in range((2*i)+1):clear
        print("*",end='  ')
    for j in range(n-i-1):
        print(" ",end='  ')
    print("\n")
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end='  ')
    for k in range((2*i)-1):
        print("*",end='  ')
    for j in range(n-i-1):
        print(" ",end='  ')
    print("\n")