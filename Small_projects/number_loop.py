number = 14
for i in range(10):
    print("Searching...")
    if number:
        print("Successful,", "The number is", number )
        break
else:
    print("Sorry, we could not find the number")