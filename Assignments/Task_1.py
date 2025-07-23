# Twitter Account Info System with User Input

# Input Details from User
w = " welcome to Twitter "
print(w)
username = input("Enter Username: ")
email = input("Enter Email: ")
Followers = float(input("Enter Followers count (0-1000): "))
interests = input("Enter Interests (comma-separated): ").split(',')
Posts = int(input("Enter Posts Count: "))
Hastags = input("Enter the Hastags:").split(',')
badges = set(input("Enter Badges (comma-separated): ").split(','))
password = input("Enter Password: ")
# Dictionary – Login credentials
login_info = {
    "username": username,
    "email": email,
    "password": password
}

print("Username, Email:", username, email, sep=',')

print("Reputation Score: %.2f%%" % Followers)

print(f"Username: @{username}")
print(f"Email: {email}")

print("Login Credentials - Username: {}, Email: {}, Password: {}".format(
    login_info["username"],
    login_info["email"],
    login_info["password"]
))

print("\nAdditional Info:")
print(f"username: {(username)}")
print(f"Interests: {', '.join(interests)}")
print(f"Hastags: {', '.join(Hastags)}")
print(f"Posts: {(Posts)}")

# Login Credentials - Username: anjanikrupal07, Email: anjani@gmail.com, Password: 123456789

#Additional Info:
#username: anjanikrupal07
#Interests: sports, movies, games
#Hastags: #salaar,  #cricket,  #pubg
#Posts: 11