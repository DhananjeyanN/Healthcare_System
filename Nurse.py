from Health_Professional import HealthProfessional


class Nurse(HealthProfessional):
    def __init__(self, employee_number):
        super().__init__(employee_number)
    def register_nurse(self):
        self.register()