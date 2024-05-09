# The code is written in Python and it allows a user to input personal information
# such as first and last names, age, email, password and address.
# This information is then stored into a tempuser dictionary that contains the entered values. 
# Using the mysql.connector library, the data is then inserted into the "users" table in a database called "pet".


#  import mysql connector module
import mysql.connector

# Connect to the MySQL server using host, username, password, and database
pet_user = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="pet"
)

# Print a connection object
print(pet_user)

# Create an empty dictionary called `tempuser`

tempuser = {
    
}

# Infinite loop that stops when there is input in First name variable, loops again if input is empty
while True:
    fname = input("First name: ")
    if fname != None and fname != "":
        tempuser["first_name"] = fname 
        break
    else:
        continue

# Infinite loop that stops when there is input in Last name variable, loops again if input is empty    
while True:
    lname = input("Last name: ")
    if lname != None and lname != "":
        tempuser["last_name"] = lname
        break
    else:
        continue

# Infinite loop that stops when there is input in Age variable, loops again if input is None or any value other than integer
while True:
    age = int(input("Age: "))
    if age != None:
        tempuser["age"] = age
        break
    else:
        continue

# Infinite loop that stops when there is input in Email Address variable, loops again if input is empty or NULL string
while True:
    email = input("Email address: ")
    if email != None and email != "":
        tempuser["email"] = email
        break
    else:
        continue

# Infinite loop that stops when there is input in Password variable, prompts user to enter password invisibly, and loops again if input is empty or NULL string.
while True:      
    from getpass import getpass
    password = getpass("Password: ")
    if password != None and password != "":
        tempuser["password"] = password
        break
    else:
        continue

# Infinite loop that stops when there is input in Address variable, loops again if input is empty or NULL string
while True:
    address = input("Address: ")
    if address != None and address != "":
        tempuser["address"] = address
        break
    else:
        continue
      
# Instantiate cursor object
curs = pet_user.cursor()

# Create SQL query and pass data through parameters using a tuple
sql = "INSERT INTO users (user_id, first_name, last_name, age, email, password, address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = (1, tempuser["first_name"], tempuser["last_name"], tempuser["age"], tempuser["email"], tempuser["password"], tempuser["address"])

# Execute query and pass parameters
curs.execute(sql, val)

# Commit changes to Database
pet_user.commit()

# Re-instantiate cursor object after commit operation                                                                   
curs = pet_user.cursor()                                                                                                  
