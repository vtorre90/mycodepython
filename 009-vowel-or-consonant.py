# In this exercise you will create a program that reads a letter of the alphabet from the user. 
# If the user enters a, e, i, o or u then your program should display a message indicating that the 
# entered letter is a vowel. If the user enters y then your program should display a message indicating 
# that sometimes y is a vowel, and sometimes y is a consonant. Otherwise your program should display 
# a message indicating that the letter is a consonant.


input_user = str(input('Write a letter\n'))


if input_user == 'a':
    print ('The entered letter is a consonant')
elif input_user == 'y':
    print ('The entered letter is a vowel and sometimes is a consonant')
else: 
    print ('The entered letter is a vowel')

