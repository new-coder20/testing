def login(password):
    if password == "123456": 
        print("Logged in!")
    else:
        print("Incorrect password")

def signup(password):
    with open("pass.txt", "a") as f:
        f.write(password + "\n")
    print("Signed up!")

print("this is not so perfect, nothing is done perfectly, another request")
