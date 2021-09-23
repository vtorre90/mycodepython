#In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them. 
# In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit, 
# and drink containers holding more than one liter have a $0.25 deposit. Write a program that reads the 
# number of containers of each size from the user. Your program should continue by computing and 
# displaying the refund that will be received for returning those containers. 
# Format the output so that it includes a dollar sign and two digits to the right of the decimal point.
#Le bottiglie fino ad 1lt pagano 0.10cent - Le bottiglie oltre al 1lt pagano 0.25 cent


print ('STARTING PROGRAM')
print ('----------------')

refound10 = 0.10
refound25= 0.25

container_small= float(input ('How many small water containers do you need?'))
container_big= float(input(('How many big water containers do you need?')))

totContainerSmall = float(refound10)*container_small
totContainerBig = float(refound25)*container_big

print ('You will get a refound equals to: ' + str(totContainerSmall+totContainerBig) +'$')


# if container_number <= 1 :
    
#     print ('You will get a refound equals to: ' + str(totRef1) +'$')
# else :
#     print ('You will get a refound equals to: ' + str(totRef2)+'$')


