Username = "admin"
Password = "python123"
username = (input("Enter your username : "))
password = (input("Enter your password : "))

if Username==username and Password==password :
    print("Login successful")
elif Username!=username:
    print("user not found")
elif password!=Password:
    print("wrong password")