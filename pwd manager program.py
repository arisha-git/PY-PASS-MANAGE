master_pwd=input("What is the password? ")

def add():
    name=input("Account Name: ")
    pwd=input("Password:")

    with open('passwords.txt', 'a') as f:
        f.write("\n" + "Account name: " + name + "\n" + "Password: " + pwd + "\n")

def view():
    pass

while True:
    mode=input("Would you like to add a new password or view existing one? (add/view/q to quit): ")
    if  mode == "q":
        break
    
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode")
    
