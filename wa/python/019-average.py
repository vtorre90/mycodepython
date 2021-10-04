
print ('\nSHORT WAY\n')
price1 = 4.95
price2 = 9.95
price3 = 14.95
price4 = 19.95
price5 = 24.95

prices = [price1, price2, price3, price4, price5]
length = len(prices)
final_price = 0
i = 0


for price in prices:
    discount = prices[i]/100 * 60
    final_price = prices[i] - discount
    price = str(round(final_price, 2))
    print(price)
    i += 1


print ('\nLONG WAY\n')


price1 = 4.95
discount1 = price1/100 * 60
final_price1 = price1 - discount1
price1_twodecimal = str(round(final_price1, 2))

print(str(price1_twodecimal) + '$')


price2 = 9.95
discount2 = price2/100 * 60
final_price2 = price2 - discount2
price2_twodecimal = str(round(final_price2, 2))

print(str(price2_twodecimal) + '$')

price3 = 14.95
discount3 = price3/100 * 60
final_price3 = price3 - discount3
price3_twodecimal = str(round(final_price3, 2))

print(str(price3_twodecimal) + '$')

price4 = 19.95
discount4 = price4/100 * 60
final_price4 = price4 - discount4
price4_twodecimal = str(round(final_price4, 2))

print(str(price4_twodecimal) + '$')

price5 = 24.95
discount5 = price5/100 * 60
final_price5 = price5 - discount5
price5_twodecimal = str(round(final_price5, 2))

print(str(price5_twodecimal) + '$')


