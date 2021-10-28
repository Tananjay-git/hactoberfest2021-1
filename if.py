is_hot = False
is_cold= False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of Water")

elif is_cold :
    print("It's a cold day")
    print("Ware wam cloths")
    
else:
    print("It's a lovely day")
    
print("Enjoy your day")


#Question :  Price of a house is $ 1M. If buyer has good credit thenneed to put down 10%. Otherwise they need to put down 20% print the down payment
# $1 in rupees = 74605300 in $ = 10,00,000

price = 1000000
has_good_credit = True

if has_good_credit :
    down_payment= 0.1*price

else:
    down_payment=0.2*price

print(f"Down Payment : ${down_payment}")
