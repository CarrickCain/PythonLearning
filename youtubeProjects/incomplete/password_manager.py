from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is your master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)




def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print("User: ", user,"\nPassword: ", fer.decrypt(passw.encode()).decode(),"\n")
def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() +"\n")

while True:
    mode = input("Would you like to add or view a password?(add, view). Press q to quit ").lower()
    
    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid Mode")