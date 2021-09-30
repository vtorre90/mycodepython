# A particular cell phone plan includes 50 minutes of air time and 50 text 
# messages for € 15.00 a month. Each additional minute of air time costs € 0.25, 
# while additional text messages cost € 0.15 each. All cell phone bills include an 
# additional charge of € 0.44 to support 911 call centers, and the entire 
# bill (including the 911 charge) is subject to 5 percent sales tax. Write a program 
# that reads the number of minutes and text messages used in a month from the user. 
# Display the base charge, additional minutes charge (if any), additional text message 
# charge (if any), the 911 fee, tax and total bill amount. Only display the additional 
# minute and text message charges if the user incurred costs in these categories. 
# Ensure that all of the charges are displayed using 2 decimal places.

#PLAN MONTH: 50 min air time + 50 text messeges  -> 15€ + 0.44€ + 5%
#ADDITION MINUTE AIR TIME: 0.25€
#ADDITION TEXT MESSAGES: 0.15€

input_minutecall = input ('Type the number of minutes\n')
input_nrmessage = input ('Type the number messages\n')

input_minutecall = int(input_minutecall)
input_nrmessage = int(input_nrmessage)

plan_base = 15
message_base= 50
cell_base=50
additional_support= 0.44
tax_value = (plan_base + additional_support)/100 * 5

#tax 5%

if (input_minutecall <= 50) and (input_nrmessage <= 50): 
    total = plan_base + additional_support + text_value
    total_formatted = "{:.2f}".format(total)
    print (total_formatted)

elif (input_nrmessage > 50):
    total2_notax = plan_base + (input_nrmessage-message_base)*0.15 + additional_support 
    tax_value = total2_notax /100 * 5
    total2 = total2_notax + tax_value
    total_formatted2 = "{:.2f}".format(total2)
    print (total_formatted2)

elif (input_minutecall > 50):
    total3_notax = plan_base + (input_minutecall-cell_base)*0.25 + additional_support
    tax_value= total3_notax/100*5
    total3 = total3_notax + tax_value
    total_formatted3 = "{:.2f}".format(total3)
    print (total_formatted3)

else 


# elif (input_minutecall > 50) and (input_nrmessage > 50): 
    
    
