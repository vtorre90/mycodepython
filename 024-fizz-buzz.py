
# If the player’s number is divisible by 3 then the player says fizz instead of their number.
# If the player’s number is divisible by 5 then the player says buzz instead of their number.

num_range = range(1,101)

for x in num_range: 
    if x %3 == 0:
        print (str(x) + ' - FIZZ')
    elif x %5 == 0:
        print (str(x) + ' - BUZZ')
    elif x %5 == 0 and x %3 == 0: 
        print (str(x) + ' - FIZZ - BUZZ')
    else: print (x)
