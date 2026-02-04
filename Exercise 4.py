user = "BachQuocHung"
password = "too"
x = 0
y = 5
while x < y:
    user = input("Enter username: ")
    password = input("Enter password: ")
    if user == "BachQuocHung" and password == "too":
        print("Login successful!")
        break
    else:
        print("Login failed. Please try again.")
        x += 1
if x == y:
    print("Maximum number of attempts reached. Exiting program.")