# This code checks a bunch of numbers to see if they're valid passwords,
# and then tells you how many valid passwords it found.

def is_valid_password(password):
    # Convert the password to a string so we can easily check each digit
    password = str(password)
    # Check if there is at least one even and one odd number
    has_even = False
    has_odd = False
    for c in password:
        if int(c) % 2 == 0:
            has_even = True
        else:
            has_odd = True
    if not has_even or not has_odd:
        return False
    # Check if the digits never decrease
    for i in range(1, len(password)):
        if int(password[i]) < int(password[i-1]):
            return False
    # Check if there are any adjacent matching digits
    for i in range(1, len(password)):
        if password[i] == password[i-1]:
            return True
    return False

# Find all passwords within the given range
start = 138345
end = 836215
count = 0
for i in range(start, end+1):
    if is_valid_password(i):
        count += 1
        print(i)
print(f"Total number of valid passwords: {count}")