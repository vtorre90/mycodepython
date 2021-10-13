# Words like first, second and third are referred to as ordinal numbers. 
# In this exercise, you will write a function that takes an integer as its only 
# parameter and returns a string containing the appropriate English ordinal number 
# as its only result. Your function must handle the integers between 1 and 12 (inclusive). 
# It should return an empty string if the function is called with an argument outside of this range. 
# Include a main program that demonstrates your function by displaying each integer from 1 to 12 
# and its ordinal number. Your main program should only run when your file has not been imported 
# into another program.

#taking user input int from 1-12

user_input = input('Write a number from 1 to 12\n')
first='first'
second='second'
third='third'
fourth='fourth'
fifth='fifth'
sixth='sixth'
seventh='seventh'
eighth='eight'
ninth='ninth'
tenth='tenth'
eleventh='eleventh'
#return string or empty string if the nr is out of the range 1-12

def tostring(num):
    if num == '1':
        return first
    elif num == '2':
        return second
    elif num == '3':
        return third
    elif num == '4':
        return fourth
    elif num == '5':
        return fifth
    elif num == '6':
        return sixth
    elif num == '7':
        return seventh
    elif num == '8':
        return eighth
    elif num == '9':
        return ninth
    elif num == '10':
        return tenth
    elif num == '11':
        return eleventh
    elif num == '12':
        return twelfth
    else: return ''

print('The ordinal number is: ' + tostring(user_input).upper())

