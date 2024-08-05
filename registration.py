print("Registration Application")
username = input("enter your username =>")
email = input("enter your email =>")
password = input("enter your password")
cpassword = input("enter your cpassword=>")
gender = input("gender (F/M/O) =>")

if username and email and password and cpassword and gender:
    if username.isalnum():
        if "@" in email and email.endswith(".com"):
            if password == cpassword:
                if len(password) >= 8:
                    print("😉🤞😉")
                else:
                    print("Password too small")
            else:
                print("Password does not match")
        else:
            print("Invaild Email")
    else:
        print("All fields are required")

