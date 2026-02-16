#Problem 3) Secure Login
import sys
# -- CORRECT VALUES -- 
correct_user = str("student")
correct_pass = str("python123")
# -- INPUT -- 
chance = 0
while chance < 3:
    print("Enter username:")
    user_user = input(">")
    print("Enter password:")
    user_pass = input(">")
    if user_user == correct_user and user_pass == correct_pass:
        print("Login Successful")
        sys.exit()
    else:
        chance = chance + 1 
        print("Invalid credentials, attempts remaining =",3 - chance)
        if len(user_pass) < 8:
            print("Security Warning: Password Too Short.")
print("Account Locked, Contact Support.")
print("End Problem 3")