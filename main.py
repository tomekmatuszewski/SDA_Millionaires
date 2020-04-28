from user.user import Admin
import time

print("Welcome in game Millionare !!!")
choice = input("Do you want to log as admin? ")
if choice == "Y":
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")
    admin = Admin(user_name, password)
    print("Logowanie...")
    time.sleep(3)
    admin.authorization()
    add_question = input("Do you want to add question to base: ")
    if add_question == "Y":
        admin.add_question()
    else:
        pass
