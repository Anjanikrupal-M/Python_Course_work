# main.py
from Data_5 import predefined_users
from Task_5 import Twitter

def menu():
    print("\n---- Twitter Application ----")
    print("1. Register Predefined Users")
    print("2. Show All Users")
    print("3. Post a Tweet")
    print("4. Follow a User")
    print("5. Show User Details")
    print("6. Exit")

# Initialize system
app = Twitter()

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        for u in predefined_users:
            app.register_user(*u)

    elif choice == "2":
        app.show_all_users()

    elif choice == "3":
        uname = input("Enter your username: ")
        post = input("Enter your tweet: ")
        user = app.find_user(uname)
        if user:
            user.add_post(post)
        else:
            print("User not found!")

    elif choice == "4":
        follower = input("Enter your username: ")
        followee = input("Enter username to follow: ")
        app.follow_user(follower, followee)

    elif choice == "5":
        uname = input("Enter username to view details: ")
        app.show_user_details(uname)

    elif choice == "6":
        print("Exiting Twitter Application. Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
