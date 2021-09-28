# A bakery sells loaves of bread for €3.49 each. Day old bread is discounted by 60 percent. 
# Write a program that begins by reading the number of loaves of day old bread being purchased 
# from the user. Then your program should display the regular price for the bread, 
# the discount because it is a day old, and the total price. Each of these amounts should be 
# displayed on its own line with an appropriate label. All of the values should be displayed using 
# two decimal places, and the decimal points in all of the numbers should be aligned when reasonable 
# values are entered by the user.

print ('Write the number of loaves you want to get')

input_loaves = int (input())

price_one_loaves = 0.30
print ('Number of choosen loaves:' + str(input_loaves))
print ('The regular price for one loave is: ' + str(price_one_loaves)+'$')
print ('The discount is: ' + str(60)+'%')


sum_loaves = price_one_loaves * input_loaves

discount_value = sum_loaves / 100 * 60

sum_loaves_discounted = sum_loaves - discount_value

print ('The discount in $ is: ' + str(discount_value))
print ('The total discounted price is: ' + str(round(sum_loaves_discounted, 3)) +'$ ' + 'for ' + str(input_loaves) + ' loaves')






