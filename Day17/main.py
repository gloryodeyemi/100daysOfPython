class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "glow")
user_2 = User("002", "ayorcodes")

user_1.follow(user_2)
print(f"User 1\n******\nFollowings: {user_1.following}\nFollowers: {user_1.followers}\n")
print(f"User 2\n******\nFollowings: {user_2.following}\nFollowers: {user_2.followers}")

# PascalCase, camelCase, snake_case
# attribute is a variable associated with an object
