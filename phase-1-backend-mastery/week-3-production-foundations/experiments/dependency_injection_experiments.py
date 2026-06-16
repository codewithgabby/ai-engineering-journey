""" class EmailService:
    def send(self):
        print("Sending email")


class UserService:

    def __init__(self):
        self.email_service = EmailService()

    def register(self):
        print("Registering user")
        self.email_service.send()


user = UserService()
user.register() """

################################################## 

""" class EmailService:

    def send(self):
        print("Sending email...")


class UserService:

    def __init__(self, email_service):
        self.email_service = email_service

    def register(self):
        print("Registering user...")
        self.email_service.send()


email = EmailService()

user = UserService(email)

user.register() """

####################################################  

