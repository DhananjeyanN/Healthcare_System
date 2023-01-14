from Employee import Employee
from Health_Professional import HealthProfessional
from Prescription import Prescription


class Doctor(HealthProfessional):
    def __init__(self, employee_number):
        super().__init__(employee_number)
        self.prescriptions = {}

    def issue_prescription(self, patient):
        prescription = Prescription("Doctor", patient, self, input("Please enter the quantity: ") , input("Please enter the dosage: "))
        patient.set_prescription(prescription)
        self.prescriptions.update({patient.first_name + patient.last_name: prescription})
    def register_doctor(self):
        self.register_employee()
