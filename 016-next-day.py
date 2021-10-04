# Write a program that reads a date from the user and computes its immediate successor. 
# For example, if the user enters values that represent 2019-11-18 then your program should display 
# a message indicating that the day immediately after 2019-11-18 is 2019-11-19. If the user enters values 
# that represent 2019-11-30 then the program should indicate that the next day is 2019-12-01. 
# If the user enters values that represent 2019-12-31 then the program should indicate that the next 
# day is 2020-01-01. The date will be entered in numeric form with three separate input statements; 
# one for the year, one for the month, and one for the day. Ensure that your program works correctly 
# for leap years.

import datetime
import calendar
from datetime import timedelta  


input_year = int(input ('Type the year\n'))
input_month = int(input ('Type the month\n'))
input_day = int(input ('Type the day\n'))

#Add 1 day  
input_date = datetime.datetime(input_year, input_month, input_day)
date_final=input_date + timedelta(days=1)

date_fin = datetime.datetime(input_year, input_month, input_day)
print (date_fin) 