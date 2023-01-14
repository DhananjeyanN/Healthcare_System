
class Prescription():
    def __init__(self, type, patient, doctor, quantity, dosage):
        self.type = type
        self.patient = patient
        self.doctor = doctor
        self.quantity = quantity
        self.dosage = dosage

    # def add_prescription(self):
    #     self.type = input("Enter prescription type: ")
    #     self.patient = Patient()
    #     self.patient.register_patient()
    #     self.doctor = Doctor()
    #     self.quantity = int(input("Enter prescription quantity: "))
    #     self.dosage = float(input("Enter prescription dosage: "))
