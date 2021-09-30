# The horoscopes commonly reported in newspapers use the position of the sun at the time of one’s birth to try and predict the future. 
# This system of astrology divides the year into twelve zodiac signs, as outline in the table below:
# Write a program that asks the user to enter his or her month and day of birth. Then your program should 
# report the user’s zodiac sign as part of an appropriate output message.

input_month = input ("Write your month of birth\n")
input_day = int(input("Write your day of birth\n"))

if input_month == 'december' and input_day > 21:
    print ('The sign is CAPRICORN')
elif input_month == 'december' and input_day < 21:
    print ('The sign is SAGGITARIUS')
    
if input_month == 'november' and input_day > 21:
    print ('The sign is SAGGITARIUS')
elif input_month == 'november' and input_day < 21:
    print ('The sign is SCORPIO')

if input_month == 'april' and input_day > 20:
    print ('The sign is TAURUS')
elif input_month == 'april' and input_day < 20:
    print ('The sign is ARIES')

if input_month == 'october' and input_day > 22:
    print ('The sign is SCORPIO')
elif input_month == 'october' and input_day < 23:
    print ('The sign is LIBRA')

if input_month == 'september' and input_day > 22:
    print ('The sign is lIBRA')
elif input_month == 'september' and input_day < 23:
    print ('The sign is VIRGO')

if input_month == 'august' and input_day > 22:
    print ('The sign is VIRGO')
elif input_month == 'august' and input_day < 23:
    print ('The sign is LEO')

if input_month == 'july' and input_day > 22:
    print ('The sign is LEO')
elif input_month == 'july' and input_day < 23:
    print ('The sign is CANCER')

if input_month == 'june' and input_day > 20:
    print ('The sign is CANCER')
elif input_month == 'june' and input_day < 22:
    print ('The sign is GEMINI')

if input_month == 'may' and input_day > 20:
    print ('The sign is GEMINI')
elif input_month == 'may' and input_day < 22:
    print ('The sign is TAURUS')

if input_month == 'april' and input_day > 19:
    print ('The sign is TAURUS')
elif input_month == 'may' and input_day < 20:
    print ('The sign is ARIES')

if input_month == 'march' and input_day > 20:
    print ('The sign is ARIES')
elif input_month == 'may' and input_day < 20:
    print ('The sign is PISCES')

if input_month == 'february' and input_day > 18:
    print ('The sign is AQUARIUS')
elif input_month == 'february' and input_day < 19:
    print ('The sign is PISCES')

if input_month == 'january' and input_day > 19:
    print ('The sign is AQUARIUS')
elif input_month == 'january' and input_day < 20:
    print ('The sign is CAPRICORN')


    

