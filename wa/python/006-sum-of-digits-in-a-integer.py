# Develop a program that reads a four-digit integer from the user and displays the sum of its digits. 
# For example, if the user enters 3141 then your program should display 3+1+4+1=9.

print ("Write a 4 digits number")

input_digits = int (input())
print (input_digits)

digits_list = [int(x) for x in str(input_digits)]

print (digits_list)

i=0
sum=0
while (i < 4):
    sum = sum + digits_list[i]
    i +=1
    

#sum = digits_list[0] +  digits_list[1] +  digits_list[2] + digits_list[3]

print ('The sum is equal to: ' + str(sum))



