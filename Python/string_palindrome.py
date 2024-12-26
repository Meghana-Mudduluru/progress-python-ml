'Write a program to check if a word is a palindrome '
a=input("Enter a word:")
#reversed string
rev=a[: : -1]
if (a==rev):
    print("The word is a palindrome")
else:
    print("The word is not palindrome")

