# In this exercise you will reverse the process described in Exercise 24. 
# Develop a program that begins by reading a number of seconds from the user. 
# Then your program should display the equivalent amount of time in the form 
# D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively. 
# The hours, minutes and seconds should all be formatted so that they occupy exactly two digits.
# Use your research skills determine what additional character needs to be included in the format 
# specifier so that leading zeros are used instead of leading spaces when a number is formatted to a 
# particular width.

# print ('Add the seconds')
# input_seconds = int (input())

# #formatting the time D:HH:MM:SS


# days = input_seconds/86400
# resto_days= input_seconds - 86400

# hours = resto_days/3600
# resto_hours=resto_days - 3600

# minutes = resto_hours/60
# resto_minutes=resto_hours - 60

# seconds = resto_minutes/60
# resto_seconds= resto_minutes - 60

# print(int(days))
# print(int(hours))
# print(int(minutes))
# print(int(seconds))

import datetime
seconds=int (input())

print(str(datetime.timedelta(seconds=seconds)))





