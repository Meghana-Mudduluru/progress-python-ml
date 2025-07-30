#1. length of string
'''
n=input("enter string:")
print("length of string is:",len(n))
'''

#2. copy one strong to another string
'''
n=input("enter string:")
copy=''
for char in n:
    copy+=char
print(f"original string is {n} and copied string is {copy}")
'''

#3. concatenate two strings
'''
n=input("enter string1:")
m=input("enter string2:")
print("total string is",n+' '+m)
'''

#4. compare two strings
'''
n=input("enter string1:")
m=input("enter string2:")
if(n==m):
    print("strings are equal")
elif(n>m):
    print(f"{n} is greater than {m}")
else:
    print(f"{m} is greater than {n}")
'''

#5. lowercase string to uppercase
'''
n=input("enter string:")
up=n.upper()
print("string in uppercase is",up)
'''

#6. uppercase string to lower case
'''
n=input("enter string:")
low=n.lower()
print("string in lowercase is",low)
'''

#7. to toggle case of each character of a string
'''
n=input("enter string:")
toggle=''
for i in n:
    if(i.islower()):
        toggle+=i.upper()
    elif(i.isupper()):
        toggle+=i.lower()
    else:
        toggle+=i
print("Toggle of string is:",toggle)
'''

#8. find total number of alphabets,digits,or spl character in a string
'''
n=input("enter string:")
alph,digit,spl=0,0,0
for i in n:
    if(i.isalpha()):
        alph+=1
    elif(i.isdigit()):
        digit+=1
    else:
        spl+=1
print(f"alphabets are {alph} , digits are {digit} , spl characters are {spl}")
'''

#9. count total number of vowels and consonants in a string
'''
n=input("enter string:")
vow=cons=0
for i in n:
    if(i.isalpha()):
        if i in 'aeiouAEIOU':
            vow+=1
        else:
            cons+=1
print(f"vowels={vow} , consonants={cons}")
'''

#10. count total no of words in string
'''
n=input('enter string:')
words=[]
words=n.split()
print(len(words))
'''

#11. reversal of string
'''
s=input('enter string:')
print(s[::-1])
'''

#12. check string is palindrome or not
'''
s=input('enter string:')
print(s[::-1])
if(s==s[::-1]):
    print("palindrome")
else:
    print("not palindrome")
'''

#13. reverse order of words in string
'''
n=input('enter string:')
words=[]
words=n.split()
print(' '.join(words[::-1]))
'''

#14. find first occurence of a character in string
'''
n=input('enter string:')
ch=input("enter the character to find:")
for i in range(len(n)):
    if(n[i]==ch):
        print(f"index is {i}")
        break
else:
    print("not found")
'''

#15. find last occurence of a character in string
'''
n=input('enter string:')
ch=input("enter the character to find:")
index=-1
for i in range(len(n)):
    if(n[i]==ch):
        index=i
if index!=-1:
    print(f"index is {i}")
else:
    print("not found")
'''
'''
n=input('enter string:')
ch=input("enter the character to find:")

for i in range(len(n)-1,-1,-1):
    if(n[i]==ch):
        print(f"index is {i}")
        break
else:
    print("not found")
'''

#16. search all occurences of chatacter in a string
'''
n=input('enter string:')
ch=input("enter the character to find:")
for i in range(len(n)):
    if(n[i]==ch):
        print(f"index is {i}")
else:
    print("not found")
'''

#17. count occurence of character in string
'''
n=input('enter string:')
ch=input("enter the character to find:")
count=0
for i in range(len(n)):
    if(n[i]==ch):
        count+=1
if(count!=0):
    print("character occurd",count,"times")
else:
    print("character not found")
'''

#18. find highest frequency character in a string
'''
string=input('enter string:')
freq_map={}
for ch in string:
    if ch in freq_map:
        freq_map[ch]+=1
    else:
        freq_map[ch]=1
maxfreq,maxchar=0,''
for ch in freq_map:
    if(freq_map[ch]>maxfreq):
        maxfreq=freq_map[ch]
        maxchar=ch
print(f"Highest freqency character in string is {maxchar} with {maxfreq} times")
'''

#19. find lowest freq character in string
'''
string=input('enter string:')
freq_map={}
for ch in string:
    if(ch!=''):
        freq_map[ch]=freq_map.get(ch,0)+1
maxfreq=min(freq_map.values())
most_freq_chars=[ch for ch in freq_map if(freq_map[ch]==maxfreq)]

print("Frequencies:", freq_map)
print("Frequency:", maxfreq)
print(f"Lowest freqency character in string is {most_freq_chars} with {maxfreq} times")
'''

#20. count freq of each character in string
'''
string=input('enter string:')
freq_map={}
for ch in string:
    if(ch!=''):
        freq_map[ch]=freq_map.get(ch,0)+1
print(freq_map)
for ch in freq_map:
    print(f"{ch}:{freq_map[ch]}")
'''

#21. remove first occurence of character from string
'''
str=input("enter string:")
r=input("enter the character u want to remove:")
final=[]
removed=False
for i in str:
    if((i==r) and not removed):
        removed=True
        continue
    final.append(i)
result=''.join(final)
print("string after removing first occureance is",result)
'''

#22. remove last occurence of character from string
'''
str=input("enter string:")
r=input("enter the character u want to remove:")
st=str[::-1]
final=[]
removed=False
for i in st:
    if((i==r) and not removed):
        removed=True
        continue
    final.append(i)
    if(i!=r):
        print("character not found")
        exit()
result=''.join(final)
print("string after removing last occurence is",result[::-1])
'''

#23. remove all occurence of character from string
'''
str=input("enter string:")
r=input("enter the character u want to remove:")
final=[]

for i in str:
    if(i!=r):
        final.append(i)
result=''.join(final)
print("string after removing first occureance is",result)
'''

#24. remove all repeated characters from a string
'''
str=input('enter string:')
freq_map={}
for ch in str:
    if ch in freq_map:
        freq_map[ch]+=1
    else:
        freq_map[ch]=1
#count freq of each character
#for ch in str:
 #   freq_map[ch]=freq_map.get(ch,0)+1
print(freq_map)
seen=set()
result=''
for ch in str:
    if(ch not in seen):
        seen.add(ch)
        result+=ch
print(result)
'''

#25. replace first occurence of character with another
'''
str=input('enter string:')
r=input('enter character u want to replace:')
re=input('enter char u want:')
st=list(str)
remove=False
for i in range(len(st)):
    if((st[i]==r) and not remove):
        remove=True
        st[i]=re
result=''.join(st)
print('string sfter replacing is',result)
'''

#26. replace last occurence of character with another
'''
str=input('enter string:')[::-1]
ch=input('enter the character u want to replace:')
ne=input('enter character u want:')
st=list(str)
replace=False
for i in range(len(st)):
    if(st[i]==ch and not replace):
        replace=True
        st[i]=ne
result=''.join(st)[::-1]
print('string after replacing:',result)
'''

#27. replace all occurence of character with another in a string
'''
str=input('enter string:')
ch=input('enter character u want to replace:')
ne=input('entr character u want:')
st=list(str)
for i in range(len(st)):
    if(st[i]==ch):
        st[i]=ne
result=''.join(st)
print("after replacing ,string is",result)
'''

#28. first occurence of word in given string
'''
str=input('input string:')
word=input('input word to search:')
index=str.find(word)
if(index!=-1):
    print('string is in index',index)
'''

#29. find last occurence of word in given string
'''
str=input('input string:')
word=input('input word to search:')
index=str.rfind(word)
if(index!=-1):
    print('string is in index',index)
'''

#30. search all occurences of word in string
'''
str=input('input string:')
word=input('input word to search:')
indices=[]
for i in range(len(str)-len(word)+1):
    if(str[i:i+len(word)]==word):
        indices.append(i)
if indices:
    print('all occurences of word are',indices)
else:
    print('word not found')
'''

#31. count occurence of a word in string
'''
str=input('input string:')
word=input('input word to search:')
indices=[]
count=0
for i in range(len(str)-len(word)+1):
    if(str[i:i+len(word)]==word):
        indices.append(i)
        count+=1
print(f"the word occured {count} times")
if indices:
    print('all occurences of word are',indices)
else:
    print('word not found')
'''

#32. remove first occurence of word from string
'''
str=input('input string:')
word=input('input word to delete:')
remove=False
for i in range(len(str)-len(word)+1):
    if ((str[i:i+len(word)]==word) and not remove):
        new=str[:i]+str[i+len(word):]
        remove=True
        break
if remove:
    print("string after removing first occurence is:",new)
else:
    print('string not found')
'''

#33. remove last occurence of word in string
'''
str=input('input string:')[::-1]
word=(input('input word to remove:'))[::-1]
remove=False
for i in range(len(str)-len(word)+1):
    if((str[i:i+len(word)]==word) and not remove):
        new=str[:i]+str[i+len(word):]
        remove=True
        break

if remove:
    print("string after removing last occurence is:", new[::-1])
else:
    print('string not found')
'''

#34. remove all occurences of word in string
'''
str=input('input string:')
word=input('input word to remove')
new=''
i=0
while(i<len(str)):
    if (str[i:i + len(word)] == word):
        i+=len(word)
    else:
        new+=str[i]
        i+=1

print('new string after removing all occurence is',new)
'''

#35. trim leading whitespace characters from a given string
'''
text = input("Enter a string: ")
result = text.lstrip()
print("String after removing leading spaces:", result)
'''

#36. trim trailing white space characters from given string
'''
text=input('input a string:')
result=text.rstrip()
print("String after removing leading spaces:", result)
'''

#37. trim both leading and trailing white space characters from given string
'''
text = input("Enter a string: ")
result = text.strip()
print("String after removing leading spaces:", result)
'''

#38. remove all blank spaces from a string
'''
str=input('input string:')
new=''
for i in str:
    if(i==' '):
        continue
    else:
        new+=i
print('string is',new)
'''

#39. remove all extra blank spaces from a string
'''
text=input('input string:')
words=text.strip().split()
new=' '.join(words)
print('string after removing extra blank spaces:',new)
'''