#1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36 -> RED
# .. -> BLACK
# 0 e 00 -> GREEN



inp = input('Type the number ')
inp = int(inp)


if (inp == 1 or inp == 3 or inp == 5 or inp == 7 or inp == 9 or inp == 12 or inp == 14 or inp == 16 or inp == 18 or inp == 19 or inp == 21 or inp == 23 or inp == 25 or inp == 27 or inp == 30 or inp == 32 or inp == 34 or inp == 36):
    print ('Pay ' + str(inp))
    print ('Pay red')
    if (inp %2 == 0):
        print ('Even')
    else: print ('Odd')
    if (inp<19):
        print ('Pay 1 to 18')
    if (inp>19):
        print ('Pay 19 to 36')
# elif (inp == 0 or inp == 00):
#     print ('Pay ' + str(inp))
#     print ('Pay green')
#     if (inp<19):
#         print ('Pay 1 to 18')
elif (inp > -1 and inp < 37):
    print ('Pay ' + str(inp))
    print ('Pay black')
    if (inp %2 == 0):
        print ('Even')
    else: print ('Odd')
    if (inp<19):
        print ('Pay 1 to 18')
    if (inp>19):
        print ('Pay 19 to 36')
else: 
    print ('ERROR: Type a valid number from 0 to 36')

