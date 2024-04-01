class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_access_level(self):
        return self.__access_level

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self.__users = []

    def add_user(self, user):
        if user not in self.__users:
            self.__users.append(user)
            print(f"User {user.get_name()} added by admin {self.get_name()}")
        else:
            print("User already exists.")

    def remove_user(self, user):
        if user in self.__users:
            self.__users.remove(user)
            print(f"User {user.get_name()} removed by admin {self.get_name()}")
        else:
            print("User not found.")

    def list_users(self):
        for user in self.__users:
            print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

# Пример использования
admin = Admin("A123", "Alice")
user1 = User("U123", "Bob")
user2 = User("U124", "Charlie")

admin.add_user(user1)
admin.add_user(user2)

admin.list_users()

admin.remove_user(user1)

admin.list_users()