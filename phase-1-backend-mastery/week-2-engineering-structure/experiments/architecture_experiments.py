""" class UserRepository:

    def save_user(self, name: str):
        print(f"Saving {name} to database")


class UserService:

    def __init__(self):
        self.user_repository = UserRepository()


    def register_user(self, name: str):

        print(f"Validating user: {name}")

        self.user_repository.save_user(name)

        print("User registration complete")


user_service = UserService()

user_service.register_user("Gabby") """

##############################################  

""" class EmailService:

    def send_welcome_email(self, name: str):
        print(f"Sending welcome email to {name}")


class UserRepository:

    def save_user(self, name: str):
        print(f"Saving {name} to database")


class UserService:

    def __init__(self):

        self.user_repository = UserRepository()

        self.email_service = EmailService()


    def register_user(self, name: str):

        print(f"Validating user: {name}")

        self.user_repository.save_user(name)

        self.email_service.send_welcome_email(name)

        print("User registration complete")


user_service = UserService()

user_service.register_user("Gabby") """ 

############################################  

class EmailService:

    def send_email(self, message: str):
        print(f"Sending email: {message}")


class UserService:

    def __init__(self, email_service: EmailService):

        self.email_service = email_service


    def register_user(self, name: str):

        print(f"Registering {name}")

        self.email_service.send_email(
            f"Welcome {name}"
        )


email_service = EmailService()

user_service = UserService(email_service)

user_service.register_user("Gabby")