x = int(input("What is your age? "))

if x >= 18 and x < 65:
    print("Your price is 10 Dollars")
elif x >= 65:
    print("With senior discount, your price is 5 Dollars")
else:
    print("Sorry, you are too young to purchase!")
