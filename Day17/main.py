class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0


user_1 = User("001", "glow")
print(user_1.id)


# PascalCase, camelCase, snake_case
# attribute is a variable associated with an object
