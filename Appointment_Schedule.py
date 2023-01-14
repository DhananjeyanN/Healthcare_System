class AppointmentSchedule:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def cancel_appointment(self, appointment):
        for app in self.appointments:
            if app.appointment_id == appointment.appointment_id:
                self.appointments.remove(app)
                print(f"Successfully removed {app}")
            else:
                print(f"Appointment could not be found with {appointment.appointment_id}")

    def find_next_appointment(self, patient):
        for appointment in self.appointments:
            if appointment.patient == patient:
                print(appointment)
