class Appointment():
    def __init__(self, app_id, patient):
        self.type = None
        self.staff = None
        self.patient = None
        self.add_appointment(patient)
        self.appointment_id = app_id


    def add_appointment(self, patient):
        self.type = input("Please enter the type of appointment you would like to make: ")
        self.staff = input("Please enter the staff's name you would like to meet: ")
        self.patient = patient
    def __str__(self):
        return f"{self.type}//{self.staff}//{self.patient}//{self.appointment_id}"