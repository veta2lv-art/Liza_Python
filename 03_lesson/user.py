class User:

    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name
        print("Пользователь создан")

    def fname(self):
        print("Имя", self.first_name)

    def lname(self):
        print("Фамилия", self.last_name)

    def fandlname(self):
        print(self.first_name, self.last_name)
