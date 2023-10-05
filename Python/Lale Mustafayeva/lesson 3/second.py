
username = "qiyascc"
user_pass = "74927"

username2 = "emildost"
user_pass2 = "qiyas"
input_user_name = input("Write username: ")

if input_user_name == username:
    true_pass = user_pass
elif input_user_name == username2:
    true_pass = user_pass2
else:
    print("False! Username not found in my database.")
    exit()

login_count = 2
while login_count >= 0:
    input_user_pass = input("Write ur password: ")

    if input_user_pass == true_pass:
        print("Succes!")
        break
    else:
        if login_count == 0:
            print("False password")
            break
        else:
            print("password not found, retry.")
            login_count -= 1
