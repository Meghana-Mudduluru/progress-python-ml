n=int(input("Enter no of rows :"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end='  ')
    for k in range((2*i)+1):
        if(k%2==0):
            print("*",end='  ')
        else:
            print(" ",end='  ')
    for j in range(n-i-1):
        print(" ",end='  ')
    print("\n")