print("Enter the credit (g/b) ")
credit=input()
price=1000000

if credit=='g': #== is comparing    have to use '' because g is a string
    total_price=price-price/10
    print(total_price)

elif credit=='b':
    total_price=price
    print(total_price)

else:
     print("Invalid input")

