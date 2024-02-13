import csv


class Person:
    def __init__(self, name, phone, nationality):
        # Runs validation on the received arguments
        assert isinstance(name, str), "NAME MUST BE A STRING!"
        assert isinstance(phone, int), "PHONE MUST BE AN INTEGER!"
        assert isinstance(nationality, str), "NATIONALITY MUST BE A STRING!"

        # Assigns attributes
        self.name = name  # Public
        self._phone = phone  # Protected
        self.__nationality = nationality  # Private

    def get_nationality(self):
        # This will return the nationality (private attribute to the Person class) inside the children classes
        return self.__nationality

    def __repr__(self):
        return f"Person('{self.name}', {self.phone}, '{self.nationality}')"


class User(Person):
    def __init__(self, name, email, phone, nationality):
        # Inherits attributes from superclass Person
        super().__init__(name, phone, nationality)
        self.email = email

    # Reads and prints the entire user database
    @classmethod
    def print_user_database(cls):
        with open("./csv/user_database.csv", "r") as f:
            reader = csv.DictReader(f)
            user_database = list(reader)

        for user in user_database:
            print(user)

    # Prints a specific user from the database
    @classmethod
    def print_user(cls, user_id):
        with open("./csv/user_database.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if int(row["id"]) == user_id:
                    print(row)
                    return  # To exit the loop when the user is found
        print(f"User ID # {user_id} not found.")

    # Adds new user to the database
    @classmethod
    def add_new_user(cls, name, email, phone, nationality):
        # Generates a new user ID
        with open("./csv/user_database.csv", "r") as f:
            reader = csv.DictReader(f)
            id_list = [int(row["id"]) for row in reader]
            new_user_id = max(id_list) + 1

        # Adds new user as new row
        with open("./csv/user_database.csv", "a", newline="") as f:
            fieldnames = ["id", "name", "email", "phone", "nationality"]
            writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_STRINGS)
            if f.tell() == 0:
                writer.writeheader()

            writer.writerow(
                {
                    "id": new_user_id,
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "nationality": nationality,
                }
            )
        print("\n--> User added successfully.\n")
