from datetime import datetime
from Classes.book import Book
from Classes.person import Person, User
from Classes.library import Library
from Functions.user import *
from Functions.book import *
from Functions.library import *


def main():
    today = datetime.today().strftime("%d/%m/%Y   %H:%M:%S")

    print("\n( ( ( Monteiro Lobato Library ) ) )\n".upper())
    print(f"Current access log: {today}")
    print
    print("--------------------------------")

    # This will print the entire user database
    get_user_database()

    # Type in the user ID to get their information from the database
    get_user_by_id(3)

    # To add a new user, enter FULL NAME, EMAIL, PHONE and NATIONALITY
    add_new_user("Anakin Skywalker", "anakin@darkside.com", 1234567891, "Tatooine")


if __name__ == "__main__":
    main()
