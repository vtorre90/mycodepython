# A particular zoo determines the price of admission based on the age of the guest. 
# Guests 2 years of age and less are admitted without charge. Children between 3 and 12 years of age cost $14.00. 
# Seniors aged 65 years and over cost $18.00. Admission for all other guests is $23.00. Create a program that begins by reading 
# the ages of all of the guests in a group from the user, with one age entered on each line. The user will enter a blank line to 
# indicate that there are no more guests in the group. Then your program should display the admission cost for the group with an 
# appropriate message. The cost should be displayed using two decimal places.


# till 2 no charge
# 3 and 12 years -> 14
# over 65 -> 18
# others -> 23


# nr_people = int(input ('How many people there are?:\n'))
zerocost = 0
fourtheen = 0
others = 0

input_age = 'a'

while input_age != "": 
    input_age = input ('Write the age:\n')

    if int(input_age) < 3 :
        zerocost += 0
    elif int(input_age) > 2 and int(input_age) < 13 : 
        fourtheen +=14
    else: 
        others += 23
print (zerocost + fourtheen  + others)
