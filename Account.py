from datetime import date

from Utilities import input_date


class Account:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.birthday = None
        self.__phone_number = None
        self.__email = None

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_phone_number(self):
        return self.__phone_number

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def register(self):
        self.first_name = input("Please enter first name: ")
        self.last_name = input("Please enter last name: ")
        self.birthday = input_date("birthday")
        self.__phone_number = input("Please enter your phone number: ")
        self.__email = input("Please enter your email: ")

# a1 = Account()
# a1.register()
# print(a1.birthday)
