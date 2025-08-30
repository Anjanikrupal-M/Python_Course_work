# logic.py
from abc import ABC, abstractmethod

# Abstraction 
class Person(ABC):
    def __init__(self, username, email):
        self._username = username   # Encapsulation: protected attribute
        self._email = email

    @abstractmethod
    def display_info(self):
        pass


# Inheritance
class User(Person):
    user_count = 0

    def __init__(self, username, email, interests):
        super().__init__(username, email)
        User.user_count += 1
        self.__followers = 0 
        self.__posts = []
        self._interests = interests

    # Polymorphism 
    def display_info(self):
        print(f"[@{self._username}] Followers: {self.__followers}, Posts: {len(self.__posts)}")

    def add_post(self, content):
        self.__posts.append(content)
        print(f"{self._username} tweeted: {content}")

    def get_posts(self):
        return self.__posts

    def add_follower(self):
        self.__followers += 1

    def get_followers(self):
        return self.__followers

    def get_username(self):
        return self._username

    @classmethod
    def total_users(cls):
        return cls.user_count

    @staticmethod
    def twitter_policy():
        return "Users must follow Twitter's community guidelines."


class Twitter:
    def __init__(self):
        self.users = {}
        print("Twitter System Initialized.")

    def register_user(self, username, email, interests):
        if username not in self.users:
            user = User(username, email, interests)
            self.users[username] = user
            print(f"User registered: {username}")
            return user
        else:
            print("Username already exists.")
            return None

    def find_user(self, username):
        return self.users.get(username)

    def follow_user(self, follower, followee):
        f1 = self.find_user(follower)
        f2 = self.find_user(followee)
        if f1 and f2:
            f2.add_follower()
            print(f"{f1.get_username()} followed {f2.get_username()}")
        else:
            print("Invalid usernames.")

    def show_all_users(self):
        for u in self.users.values():
            u.display_info()

    def show_user_details(self, username):
        user = self.find_user(username)
        if user:
            print(f"\nProfile: {user.get_username()}")
            print(f"Email: {user._email}")
            print(f"Followers: {user.get_followers()}")
            print(f"Posts: {user.get_posts()}")
            print(f"Interests: {', '.join(user._interests)}")
        else:
            print("User not found.")
