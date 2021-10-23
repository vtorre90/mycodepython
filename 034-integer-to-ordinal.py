# Words like first, second and third are referred to as ordinal numbers. In this exercise, you will write a function that takes an integer as its only parameter and returns a string containing the appropriate English ordinal number as its only result. Your function must handle the integers between 1 and 12 (inclusive). It should return an empty string if the function is called with an argument outside of this range. Include a main program that demonstrates your function by displaying each integer from 1 to 12 and its ordinal number. Your main program should only run when your file has not been imported into another program.

# user input
inp = input('Write a number in between 1-12:\n')


# function definition
def ordinalNr(inp):

    if inp == '1':
        return 'First'

    elif inp == '2':
        return 'Second'

    elif inp == '3':
        return 'Third'

    elif inp == '4':
        return 'Fourth'

    elif inp == '5':
        return 'Fifth'
    
    elif inp == '6':
        return 'Sixth'

    elif inp == '7':
        return 'Seventh'

    elif inp == '8':
        return 'Eighth'

    elif inp == '9':
        return 'Ningth'

    elif inp == '10':
        return 'Tenth'

    elif inp == '11':
        return 'Eleventh'

    elif inp == '12':
        return 'Twelfth'

    else:
        return 'Write a valid number'


# output
print('The ordinal number is: ' + ordinalNr(inp))