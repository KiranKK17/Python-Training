#PASSWORD CREATION
def authenticate():
    password="ammulu1404"
    attempts=3
    while attempts>0:
        user_input=input("enter password")
        if user_input==password:
            print("welcome")
            break
        else:
            attempts-=1
            if attempts>0:
                print(f"wrong password! You have {attempts} attempts left.")
            else:
                print("Account blocked")
                break
authenticate()
