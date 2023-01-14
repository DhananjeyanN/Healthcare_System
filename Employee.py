import datetime

import Utilities
from Account import Account
from datetime import date


class Employee(Account):
    def __init__(self, employee_number):
        super().__init__()
        self.__pay_rate = None
        self.__hours_worked_week = None
        self.__date_joined = None
        self.experience = None
        self.__pay = None
        self.__employee_num = employee_number


    def calculate_pay(self):
        return (self.__hours_worked_week * self.__pay_rate) * 2

    def set_increment(self):
        if self.experience >= 1:
            self.__pay_rate += self.__pay_rate * .05

    def get_pay(self):
        return (self.__pay)

    def get_pay_rate(self):
        return self.__pay_rate

    def set_pay_rate(self, payrate = None):
        if payrate is None:
            new_rate = float(input("Enter new pay rate: "))
        else:
            new_rate = payrate
        self.__pay_rate = new_rate

    def get_hours_worked_week(self):
        return self.__hours_worked_week

    def set_hours_worked_week(self, hours = None):
        if hours is None:
            new_hours = float(input("Enter new hours worked per week: "))
        else:
            new_hours = hours

        self.__hours_worked_week = new_hours

    def get_date_joined(self):
        return self.__date_joined

    def set_date_joined(self, input_date = None):
        if input_date is None:
            self.__date_joined = Utilities.input_date("joining date")
        else:
            self.__date_joined = input_date

    def find_experience(self):
        d_t = datetime.datetime.today()
        if d_t.month < self.__date_joined.month:
            self.experience = (datetime.datetime.today().year - self.__date_joined.year) - 1
        else:
            self.experience = (datetime.datetime.today().year - self.__date_joined.year)
        return self.experience

    def set_employee_number(self, employee_number):
        self.__employee_num = employee_number

    def get_employee_number(self):
        return self.__employee_num

    def set_pay(self, pay):
        self.pay = pay
    def register_employee(self):
        self.register()
        self.set_pay_rate()
        self.set_date_joined()
        self.set_hours_worked_week()
        self.experience = self.find_experience()
        self.__pay = self.calculate_pay()
        self.set_increment()

