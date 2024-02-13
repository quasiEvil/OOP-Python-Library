from Classes.person import Person, User


def get_user_database():
    print("\nUser database:".upper())
    User.print_user_database()


def get_user_by_id(id):
    print(f"\nHere is the user information:".upper())
    User.print_user(id)


def add_new_user(name: str, email: str, phone: int, nationality: str):
    User.add_new_user(name, email, phone, nationality)
