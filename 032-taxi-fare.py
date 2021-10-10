# In a particular jurisdiction, taxi fares consist of a base fare of €4.00, plus €0.25 for every 140 meters travelled. 
# Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare as its only result. 
# Write a main program that demonstrates the function.

base_fare=4
# 0.25€ ogni 140mt   140:025 = 1000:x

def totFare():
    inp = int(input('Write the distance in kilometers: '))
    fare_kilometre=1000*0.25 / 140
    tot_kil = base_fare + (fare_kilometre* inp)
    total = str(round(tot_kil, 2))
    return total

print ('The total fare is: ' + str(totFare()) + '€')
