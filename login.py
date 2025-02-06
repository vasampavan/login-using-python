import getpass
database = {"pavan":"12345","user":"password"}
while(1):
    username = input("Enter Your Username : ")
    if username not in database:
        password=getpass.getpass("Create Password")
        database[username]=password
        print("Account created")
    else:
        password = getpass.getpass("Enter Your Password : ")
        for i in database.keys():
            if username == i:
                while password != database.get(i):
                    password = getpass.getpass("Enter Your Password Again : ")
                break
        print("Verified")
    userinput=input("Do you want to continue(Y/N)")
    if(userinput=="N"):
        break
    
