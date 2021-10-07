
#input from user 
inp = input ('Type a world\n')
print (inp)

#from string to list
list1=[]
list1[:0]=inp
print(list1)

#create list copy to pass by value (not reference)
list2 = list1.copy()

#copy each value to the new list
j = len(list1)
for x in range (len(list2)): 
    list2[x] = list1[j-1]
    j -= 1
print (list2)



