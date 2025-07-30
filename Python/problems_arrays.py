#1. read and print elements of list
'''
list=[]
n=int(input('enter no of elements in the list:'))
for i in range(n):
    item=input(f'enter the {i} element:')
    list.append(item)
print("The elements in the list are:")
for i,item in enumerate(list,start=0):
    print(f"Element{i}:{item}")
'''

#2. print all negative numbers in list
'''
list=list()
n=int(input('enter no of elements in the list:'))
found=False
for i in range(n):
    item=input('enter element:')
    list.append(item)
    
for i in range(len(list)):
    if(int(list[i])<0):
        print(list[i],end=' ')
        found=True

if not found:
    print('no negative element')
'''

#3. find sum of all list elements
'''
list=list()
n=int(input('enter no of elements in the list:'))
sum=0
for i in range(n):
    item=input('enter element:')
    list.append(item)

for num in list:
    sum+=int(num)
print("The sum of all list elements is:",sum)
'''

#4. find maximum and minimum element in list
'''
list=list()
n=int(input('enter no of elements in the list:'))

for i in range(n):
    item=int(input('enter element:'))
    list.append(item)

maximum=minimum=list[0]
for num in list[1:]:
    if(num>maximum):
        maximum=num
    if(num<minimum):
        minimum=num

print("the max number is:",maximum)
print("the min number is:",minimum)
'''

#5. find second largest element in a list
'''
list=list()
n=int(input('enter no of elements in the list:'))

for i in range(n):
    item=int(input('enter element:'))
    list.append(item)

final=sorted(list)
print(final)
print("The second largest element in the list is:",list[-2])
'''

#6. count total no of even and odd elements in a list
'''
list=list()
n=int(input('enter no of elements in the list:'))

for i in range(n):
    item=int(input('enter element:'))
    list.append(item)

even=odd=0
for num in list:
    if(num%2==0):
        even+=1
    else:
        odd+=1
print(f"even elemnts are {even} and odd elements are {odd}")
'''

#7. count total no of neg elements in list
'''
list=list()
n=int(input('enter no of elements in the list:'))

neg,count=False,0
for i in range(n):
    item=int(input('enter element:'))
    list.append(item)
for num in list:
    if(num<0):
        count+=1
        neg=True

print(f"there are {count} neg elements in list")
if not neg:
    print('no neg numbers in list')
'''

#8. copy all elements from a list to another list
'''
list=list()
n=int(input('enter no of elements in the list:'))

for i in range(n):
    item=int(input('enter element:'))
    list.append(item)
#copying to another list
list2=[]
for num in list:
    list2.append(num)

print("original list:",list)
print("copied list:",list2)
'''

#9. insert an element in a list
'''
list=list()
n=int(input('enter no of elements in the list:'))

for i in range(n):
    item=int(input('enter element:'))
    list.append(item)
element=input('enter the element u want to insert:')
index=int(input('at what index u want to insert:'))
list.insert(index,element)
print(f"the final list is:{list}")
'''

#10. delete an element from a list at specified position
'''
list=list()
n=int(input('enter no of elements in the list:'))

for i in range(n):
    item=int(input('enter element:'))
    list.append(item)

print(list)
pos=int(input("enter the position to delete:"))
if(0<=pos<len(list)):
    list.pop(pos)

print(f"after removing element , the list is {list}")
'''

#11. count frequency of each element in a list
'''
list=list()
n=int(input('enter no of elements in the list:'))

for i in range(n):
    item=input('enter element:')
    list.append(item)
print(list)
freq_map={}
for item in list:
    if item!='':
        freq_map[item]=freq_map.get(item,0)+1
print("The count of elemnts are:",freq_map)

for item in freq_map:
    print(f"{item} : {freq_map[item]}")
'''

#12. print all unique elements in the list
'''
list=list()
n=int(input('enter no of elements in the list:'))
for i in range(n):
    item=input('enter the element:')
    list.append(item)
print(list)

freq_map={}
for item in list:
    if item!='':
        freq_map[item]=freq_map.get(item,0)+1
print(freq_map)

print("Unique element in list :")
for i in freq_map:
    if(freq_map[i]==1):
        print(i,end='\t')
'''

#13. count total number of duplicate elements in the list
'''
list=list()
n=int(input('enter no of elements in the list:'))
for i in range(n):
    item=input('enter the element:')
    list.append(item)
print(list)

freq_map={}
for item in list:
    if item!='':
        freq_map[item]=freq_map.get(item,0)+1
print(freq_map)
dup=0
for key in freq_map:
    if(freq_map[key]!=1):
        dup+=freq_map[key]-1
print(f"Duplicate elements in the list are:",dup)
'''

#14. delete all duplicate elements from list
'''
list=list()
n=int(input('enter no of elements in the list:'))
for i in range(n):
    item=input('enter the element:')
    list.append(item)
print(list)

unique=[]
for item in list:
    if item not in unique:
        unique.append(item)

print("Unique list is :",unique)
'''

#15. merge two list to third list
'''
list1=list()
n=int(input('enter no of elements in the list1:'))
for i in range(n):
    item=input('enter the element:')
    list1.append(item)
print(list1)
list2=list()
n=int(input('enter no of elements in the list2:'))
for i in range(n):
    item=input('enter the element:')
    list2.append(item)
print(list2)

list3=list2+list1
print(list3)
print("Sorted list :",sorted(list3))
'''

#16. find reverse of a list
'''
list1=list()
n=int(input('enter no of elements in the list1:'))
for i in range(n):
    item=input('enter the element:')
    list1.append(item)
print(list1)

print(list1[::-1])
'''

#17. put even and odd elements of a list in two seperate list
'''
list1=list()
n=int(input('enter no of elements in the list1:'))
for i in range(n):
    item=input('enter the element:')
    list1.append(item)
print(list1)
list2=list()
list3=list()
for i in list1:
    if((int(i)%2)==0):
        list2.append(i)
    else:
        list3.append(i)
print(f"even list:",list2)
print(f"odd list:",list3)
'''

#18. search an element in a list
'''
list1=list()
n=int(input('enter no of elements in the list:'))
for i in range(n):
    item=input('enter element:')
    list1.append(item)
print(list1)
search=input('enter the element u want to search:')
for i,item in enumerate(list1):
    if(item==search):
        print(f"{item} is found at {i} place")
'''

#19. sort list elements in ascending or descending order
'''
list1=list()
n=int(input('enter no of elements in the list:'))
for i in range(n):
    item=input('enter element:')
    list1.append(item)
print(list1)

asc=sorted(list1)
des=sorted(list1,reverse=True)

print('ascending:',asc)
print('descending:',des)
'''

#20. sort even and odd elements of list seperately
'''
list1=list()
n=int(input('enter the no of elements in list:'))
for i in range(n):
    item=input('enter the element:')
    list1.append(item)
print(list1)
list2=[]
list3=[]
for i in list1:
    if(int(i)%2==0):
        list2.append(i)
    else:
        list3.append(i)
print(f"even list after sorted={sorted(list2)}")
print(f"odd list after sorted={sorted(list3)}")
'''

#21. left rotate a list
'''
list1=list()
n=int(input('enter no of elements in the list:'))
for i in range(n):
    item=input('enter element:')
    list1.append(item)
print(list1)
index=int(input('enter no of positions to rotate left:'))
print(f'after rotating left , final array is {list1[index:len(list1)] + list1[:index]}')
'''

#22. right rotate a list
'''
list1=list()
n=int(input('enter no of elements in list:'))
for i in range(n):
    item=input('enter element:')
    list1.append(item)
print(list1)
index=int(input('enter no of positions to rotate right:'))
index=index%len(list1)
print(f'after rotating right , final array is {list1[-index:] + list1[:-index]}')
'''
