# Positions on a chess board are identified by a letter and a number. The letter identifies the column, 
# while the number identifies the row, as shown below.
# Write a program that reads a position from the user. Use an if statement to determine 
# if the column begins with a black square or a white square. Then use modular arithmetic to report 
# the color of the square in that row. For example, if the user enters a1 then your program should 
# report that the square is black. If the user enters d5 then your program should report that the 
# square is white. Your program may assume that a valid position will always be entered. It does not 
# need to perform any error checking.

#user input
input_position = input('Inserisci una lettera e un numero\n') 
inp = input_position

#conversion to separat the characters
def spacing (string):
    return ' '.join(string)

inp_space = (spacing(inp))
length = (len(inp_space) -1)

#conversion to a list 
def convert (string):
    li = list (string.split(" "))
    return li

#checking the colors
if int(inp_space[-1]) < 9 and length < 3: 
    if inp_space[0] == 'a' or inp_space[0] == 'c' or inp_space[0] == 'e' or inp_space[0] == 'g':
        print ('column starts with black\n')
        if int(inp_space[-1]) %2 == 0:
            print ('the square is white')
        elif int(inp_space[-1]) %2 != 0:
            print ('the square is black')
    else: 
        print ('Write a valid position')

    if inp_space[0] == 'b' or inp_space[0] == 'd' or inp_space[0] == 'f' or inp_space[0] == 'h':
        print ('column starts with white\n')
        if int(inp_space[-1]) %2 != 0:
            print ('the square is white')
        elif int(inp_space[-1]) %2 == 0:
            print ('the square is black')
    else: 
        print ('Write a valid position')
else: 
    print ('Write a valid position')





