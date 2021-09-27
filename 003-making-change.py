# Consider the software that runs on a self-checkout machine. 
# One task that it must be able to perform is to determine how much change to provide 
# when the shopper pays for a purchase with cash. Write a program that begins by reading 
# a number of cents from the user as an integer. Then your program should compute and display 
# the denominations of the coins that should be used to give that amount of change to the shopper. 
# The change should be given using as few coins as possible. Assume that the machine is loaded 
# with pennies, nickels, dimes, quarters, loonies and toonies.

#pennies 1 penny= $0.01
#nickels: 1 nickel= $0.05
#dimes: $0.10
#quarters: $0.25
#loonies: ?
#toonies: ?
 
# reading a number of cents from the user as an integer
print ("The total is: 23$. Add your cash amount:")

total=23
penny=0.01
user_input = float(input())

change = abs(total - user_input)

print ("The change is: " + str(change))
change_coins= change/penny
print ("You will get this amount of coins: " + str(int(change_coins)))