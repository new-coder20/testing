def login(password):
    if password == "123456": 
        print("Logged in!")
    else:
        print("Incorrect password")

def signup(password):
    with open("pass.txt", "a") as f:
        f.write(password + "\n")
    print("Signed up!")

login("123456")
signup("123456")
signup("123457")
    