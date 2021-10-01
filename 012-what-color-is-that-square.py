# Positions on a chess board are identified by a letter and a number. The letter identifies the column, 
# while the number identifies the row, as shown below.
# Write a program that reads a position from the user. Use an if statement to determine 
# if the column begins with a black square or a white square. Then use modular arithmetic to report 
# the color of the square in that row. For example, if the user enters a1 then your program should 
# report that the square is black. If the user enters d5 then your program should report that the 
# square is white. Your program may assume that a valid position will always be entered. It does not 
# need to perform any error checking.

#getting input from user
user_input = input ('Add one letter and one number\n')

#split the characters
splitted_input = ' '.join(user_input)
print(splitted_input + '\n')

char = splitted_input[0]
number = int (splitted_input[-1])

#change a character to number
char = int(ord(char)-96)


# #change a character to numberi
if number < 9: 
    if char %2 == 0 and number %2 == 0: 
        print('Square is black')
    if char %2 != 0 and number %2 != 0:
        print('Square is black')
    elif char %2 != 0 and number %2 == 0:
        print('Square is white')
    elif char %2 == 0 and number %2 != 0:
        print('Square is white')
else: 
    print ('Write a valid number')



