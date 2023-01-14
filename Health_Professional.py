from Appointment import Appointment
from Employee import Employee


class HealthProfessional(Employee):
    def __init__(self, employee_number):
        super().__init__(employee_number)
        self.availabilities = []
        self.appointments = []
    def add_availability(self):
        date = input("Enter your available day: ")
        time = input("Enter your available time: ")
        availability = {"date": date, "time": time, "Booked":False}
        self.availabilities = []
        self.availabilities.append(availability)

    def add_appointment(self, date, time, appointment_id, patient):
        for i in self.availabilities:
            print(i)
            if i["date"] == date and i["time"] == time and i["Booked"] == False:
                i["Booked"] = True
                appointment = Appointment(appointment_id, patient)
                appointment.add_appointment()
                self.appointments.append(appointment)
            else:
                print("Sorry not available")

    def show_availability(self):
        for i in self.availabilities:
            print(i)




