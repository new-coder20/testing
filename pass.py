def login(password):
    if password == "secret-password": 
        print("Logged in!")
    else:
        print("Incorrect password")

def signup(password):
    with open("pass.txt", "a") as f:
        f.write(password + "\n")
    print("Signed up!")

print("use hashed passwords, issue is that we are handling credientials without security")

    
