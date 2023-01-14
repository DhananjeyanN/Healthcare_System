from Account import Account
from Appointment import Appointment


class Patient(Account):
    def __init__(self, patient_id):
        super().__init__()
        self.patient_id = patient_id
        self.address = None
        self.prescription = None
        self.prescriptions = []
        self.appointment = None

    def register_patient(self):
        self.register()
        self.address = input("Please enter your address: ")

    def set_prescription(self, prescription):
        self.prescription = prescription
        self.prescriptions.append(self.prescription)

    def request_repeat_prescription(self):
        self.prescription.type = "repeat"
        self.prescription.append(self.prescription)

    def request_appointment(self):
        self.appointment = Appointment()
        self.appointment.add_appointment()
        return self.appointment

