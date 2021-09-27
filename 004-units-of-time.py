# Create a program that reads a duration from the user as a number of days, hours, minutes, and seconds. 
# Compute and display the total number of seconds represented by this duration.

print ("Add the number of days")
nr_days = int(input())
days_seconds= nr_days* 86400

print ("Add the number of hours")
nr_hours = int(input())
hours_seconds= nr_hours*3600

print ("Add the number of minutes")
nr_minutes = int(input())
hours_minutes= nr_hours*60

print ("Add the number of seconds")
nr_seconds = int(input())

tot_seconds=days_seconds+hours_seconds+hours_minutes+nr_seconds

print ("Il numero tot di secondi è: " +  str(tot_seconds))
