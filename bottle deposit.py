#In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them. 
# In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit, 
# and drink containers holding more than one liter have a $0.25 deposit. Write a program that reads the 
# number of containers of each size from the user. Your program should continue by computing and 
# displaying the refund that will be received for returning those containers. 
# Format the output so that it includes a dollar sign and two digits to the right of the decimal point.

print ('STARTING PROGRAM')
print ('----------------')

refound1 = 0.10
refound2= 0.25

container_number = float(input ('How many water containers do you need? '))

totRef1 = float(refound1)*container_number
totRef2 = float(refound2)*container_number

if container_number <= 1 :
    
    print ('You will get a refound equals to: ' + str(totRef1) +'$')
else :
    print ('You will get a refound equals to: ' + str(totRef2)+'$')


