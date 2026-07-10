username = input("Enter Username: ")
password = input("Enter Password: ")

# Hardcoded Credentials
admin_username = "admin"
admin_password = "12345"

if username == admin_username and password == admin_password:
    print("Login Successful")
else:
    print("Login Failed")
  
