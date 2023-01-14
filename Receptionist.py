from Appointment import Appointment
from Employee import Employee


class Receptionist(Employee):
    def __init__(self, appointment_schedule, employee_number):
        super().__init__(employee_number)
        self.appointment_schedule = appointment_schedule

    def make_appointment(self, patient, doctor):
        app_id = len(self.appointment_schedule.appointments) + 1
        appointment = Appointment(app_id, patient)
        self.appointment_schedule.add_appointment(appointment)
        print("Appointment has been created")

    def cancel_appointment(self):
        appointment_id = input("Enter id#: ")
        self.appointment_schedule.cancel_appointment(appointment_id)

    def register_receptionist(self):
        self.register_employee()
