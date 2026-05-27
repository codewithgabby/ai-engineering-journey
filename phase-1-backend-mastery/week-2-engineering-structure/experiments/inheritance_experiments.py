""" class User:

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


    def login(self):
        print(f"{self.name} logged in")


class Admin(User):

    def delete_user(self):
        print(f"{self.name} deleted a user")


admin1 = Admin("Gabby", "gabby@gmail.com")

admin1.login()

admin1.delete_user() """

##################################### 

""" class User:

    def __init__(self, name: str):
        self.name = name


    def login(self):
        print(f"{self.name} logged in")


class Admin(User):

    def delete_user(self):
        print(f"{self.name} deleted a user")


class Customer(User):

    def buy_product(self):
        print(f"{self.name} bought a product")


admin1 = Admin("Gabby")

customer1 = Customer("John")

admin1.login()
admin1.delete_user()

customer1.login()
customer1.buy_product() """

###################################### 

""" class User:

    def login(self):
        print("User logged in")


class Admin(User):

    def login(self):
        print("Admin logged in with extra security")


user1 = User()

admin1 = Admin()

user1.login()

admin1.login() """

#############################################

""" class NotificationService:

    def send_email(self, message: str):
        print(f"Sending email: {message}")


class User:

    def __init__(self, name: str):
        self.name = name
        self.notification_service = NotificationService()


    def login(self):

        print(f"{self.name} logged in")

        self.notification_service.send_email(
            f"{self.name} logged into the system"
        )


user1 = User("Gabby")

user1.login() """