# The length of a month varies from 28 to 31 days. In this exercise you will create a program that 
# reads the name of a month from the user as a string. Then your program should display the number of 
# days in that month. Display “28 or 29 days” for February so that leap years are addressed.

# 28 days: february 
# 30 days: november, april, june , september 
# 31 days: january, march, may, july, august, october

input_user = str(input("Type the month\n"))
input = input_user.capitalize()


if input == 'february':
    print (str(input) + ' has 28 or 29 days')

elif input == 'november' or 'april' or 'june' or 'september':
    print (str(input) + ' have 30 days')

elif input == 'january' or 'march' or 'may' or 'july' or 'august' or 'october':
    print (str(input) + ' have 31 days')


