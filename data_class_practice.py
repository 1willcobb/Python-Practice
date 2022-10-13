"""
Will's Practice shit
"""
import random
import string

def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


class Users:
    
    def __init__(self, first_name: str, last_name: str, email: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.active = True
        self.log_in_attempts = 0
        self.back_pack = ["sando", "knife", "dragon"]
        self.full_name = first_name + " " + last_name


    def describe_user(self) -> None:
        print(f"User Name = {self.first_name} {self.last_name}\n"
              f"Email = {self.email}\n"
              f"Phone = {self.phone}\n"
              f"Active = {self.active}")

    def greet_user(self) -> None:
        print(f"Hello {self.full_name}")

    def increment_login_attempts(self):
        self.log_in_attempts += 1

    def reset_login(self):
        self.log_in_attempts = 0

    def get_log_in_attempts(self):
        print(self.log_in_attempts)

    def __delete__(self):
        print("Deleted")

    def __str__(self) -> str:
        return f"User: {self.full_name}, Active user status: {self.active}."
    
class Privileges:

    def __init__(self) -> None:
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"This administrator has the following privilages:\n")
        print(*self.privileges, sep='\n')

class Admin(Users):

    def __init__(self, first_name, last_name, email, phone):
       super().__init__(first_name, last_name, email, phone)
       self.privileges = Privileges()
       self.admin = True

    def describe_admin(self):
        print(f"")


def main() -> None:
    user_1 = Admin("Will", "Cobb", "cobb.will@gmail.com", "(678) 446 7207")
    user_1.describe_user()


    # user_1.privileges.show_privileges()

if __name__ == "__main__":
    main()