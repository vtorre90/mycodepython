# The length of a month varies from 28 to 31 days. In this exercise you will create a program that 
# reads the name of a month from the user as a string. Then your program should display the number of 
# days in that month. Display “28 or 29 days” for February so that leap years are addressed.

# 28 days: february 
# 30 days: november, april, june , september 
# 31 days: january, march, may, july, august, october

inp = input("Type the month")

if inp == 'february':
    print (inp + ' has 28 or 29 days')

elif inp == 'november' or inp =='april' or inp =='june' or inp =='september':
    print (inp + ' have 30 days')

elif inp == 'january' or inp =='march' or inp =='may' or inp =='july' or inp =='august' or inp =='october' or inp =='december':
    print (inp + ' have 31 days')

else: 
    print ("Type the name of a month")


