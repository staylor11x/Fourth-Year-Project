'''
    This file will provide the login verification for the Local DCS

    Created:    19/12/2021
    Developer:  Scott Taylor

    Future Work:
    -- On login take user to relevant homepage based on permission
    -- notification sent to relevant parties on x number of failed login attempts
    -- password hash scrambling
'''
import time

#crate database to store user login information 
users = {
    "Engineer"  :("ENGPASS", "ENG"),
    "CRO"       :("CROPASS", "CRO"),
    "Admin"     :("ADMINPASS", "ADM"),
}

#fucntion to check login credentials
def login(username, password):
    #check if the username exists in the database
    if username in users:
        #retrive the username and password information from dic
        password_hash, permission = users[username]
        if(password_hash == password):
            return permission 
        else:
            return None
    else:
        return None

attempts = 0
max_attempts = 3
while True:
    #promt the user for login credentials
    username = input("Enter Usename: \n")
    password = input("Enter Password: \n")

    #check the input against the stored data
    permission = login(username, password)

    if(permission == None) & (attempts < max_attempts):
        print("Acess Denied, Please Enter a valid usename and password combination\n")
        attempts +=1
    elif attempts == max_attempts:
        timer = 30
        attempts = 0
        while timer > 0:
            print("Too many attempts please wait {}s... \n".format(timer))
            timer -=1
            time.sleep(1)
    else:
        print("Acess Granted {}! Permission level {}".format(username, permission))
        attempts = 0
        break
