# Positions on a chess board are identified by a letter and a number. The letter identifies the column, 
# while the number identifies the row, as shown below.
# Write a program that reads a position from the user. Use an if statement to determine 
# if the column begins with a black square or a white square. Then use modular arithmetic to report 
# the color of the square in that row. For example, if the user enters a1 then your program should 
# report that the square is black. If the user enters d5 then your program should report that the 
# square is white. Your program may assume that a valid position will always be entered. It does not 
# need to perform any error checking.

# #1-8 & a-h


input_position = input('Type the position\n') 
inp = input_position

#conversion to separated cha
# racters
def spacing (string):
    return ' '.join(string)

inp_space = (spacing(inp))


#conversion to a list 
def convert (string):
    li = list (string.split(" "))
    return li

print ('This is the typed position:\n')
print (convert(inp_space))

str(inp_space[0])

length = (len(inp_space) -1)

if int(inp_space[-1]) < 9 and length < 3:
    if int(inp_space[-1]) %2 == 0 and (inp_space[0] == 'a' or 'c' or 'e' or 'g'):
        print ('The space is white')
    elif int(inp_space[-1]) %2 != 0 and (inp_space[0] == 'b' or 'd' or 'g' or 'h'): 
        print ('The space is black')
else: 
    print ('Write a valid position')





