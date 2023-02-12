# A beginner project to validate a Username and password

import time


username = input('Username?: ')
password = input('Password?: ')

if username == "Abdullahi" and password == "1234":
    print("Access granted")
    print("Please wait")
    time.sleep(3)
    print('...')
    time.sleep(1)
    print('Okay Loading...')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('Okay you have security clearance, pulling up the secret mainframe')

elif username == "Abdullahi" and password != "1234":
    print("...")
    time.sleep(2)
    print("Password Incorrect")

elif username != "Abdullahi" and password == "1234":
    print("...")
    time.sleep(2)
    print("Retype the username correctly")

elif username != "Abdullahi" and password != "1234":
    print("...")
    time.sleep(2)
    print("Username and password are incorrect")
else:
    print("you might wanna check both fields")    
    
    
