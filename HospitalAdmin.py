from Appointment_Schedule import AppointmentSchedule
from Nurse import Nurse
from Patient import Patient
from Receptionist import Receptionist
from Doctor import Doctor
from csv import reader, writer


class HospitalAdmin():
    def __init__(self):
        self.appointments_schedules = AppointmentSchedule()
        self.employees = []
        self.receptionist = Receptionist(self.appointments_schedules, len(self.employees)+1)
        self.doctors = []
        self.nurses = []
        self.patients = []
        self.receptionists = []
        self.load_data("Doctors.csv", "Doctor")
        print(self.doctors)
        self.load_data("Nurses.csv", "Nurse")
        self.load_data("Patients.csv", "Patient")
        self.load_data("Receptionists.csv", "Receptionist")


    def dashboard(self):
        menu = """
        1:Manage Appointments
        2:Health Professional
        3:Patient
        4:Employee Management
        5:Exit
        """
        choice = None
        while choice != "5":
            choice = input(menu)
            if choice == "1":
                self.appointment_dashboard()
            elif choice == "2":
                self.health_professional_dashboard()
            elif choice == "3":
                self.patient_dashboard()
            elif choice == "4":
                self.employee_management_dashboard()

    def appointment_dashboard(self):
        menu = """
        1:Add Appointment
        2:Cancel Appointment
        3:Exit
        """
        choice = None
        while choice != "3":
            choice = input(menu)
            if choice == "1":
                patient_id = int(input("Please enter patient id: "))
                for patient in self.patients:
                    if patient.patient_id == patient_id:
                        choice1 = input("1:Doctor // 2:Nurse ")
                        if choice1 == "Doctor":
                            choice2 = input("Enter Doctor's id#:")
                            for doctor in self.doctors:
                                if doctor.get_employee_number() == choice2:
                                    print(doctor.availabilities)
                                    doctor.add_appointment(input("Please enter date"), input("Please enter time"),
                                                           len(doctor.appointments) + 1, patient)
                                    print(doctor.appointments)
                        elif choice1 == "Nurse":
                            choice2 = input("Enter Nurse's id#:")
                            for nurse in self.nurses:
                                if nurse.get_employee_number() == choice2:
                                    nurse.add_appointment(input("Please enter date"), input("Please enter time"),
                                                          input("Please enter appointment id: "), patient)
                                    print(nurse.appointments)
            elif choice == "2":
                patient_id = int(input("Please enter patient id: "))
                for patient in self.patients:
                    if patient.patient_id == patient_id:
                        self.receptionist.cancel_appointment(patient)

    def health_professional_dashboard(self):
        dashboard = """
        1:Add Doctor
        2:Add Nurse
        3:Doctor
        4:Nurse
        5:Exit
        """
        choice = None
        while choice != "5":
            choice = input(dashboard)
            if choice == "1":
                doctor = Doctor(len(self.employees) + 1)
                doctor.register_doctor()
                self.doctors.append(doctor)
                self.save_data("Doctors.csv", self.doctors, ["Employee ID", "First Name", "Last Name", "Birthday"
                    , "Phone Number", "Email", "Pay", "Hours Worked Week"
                    , "Date Joined", "Experience", "Availability", "Appointments", "Prescriptions"],
                               "Doctor")
            elif choice == "2":
                nurse = Nurse(len(self.employees) + 1)
                nurse.register_nurse()
                self.nurses.append(nurse)
                self.save_data("Nurses.csv", self.nurses, ["Employee ID", "First Name", "Last Name", "Birthday"
                    , "Phone Number", "Email", "Pay", "Hours Worked Week"
                    , "Date Joined", "Experience", "Availability", "Appointments"], "Nurse")
                self.nurses.append(nurse)
            elif choice == "3":
                self.doctor_dashboard()
            elif choice == "4":
                self.nurse_dashboard()

    def employee_management_dashboard(self):
        dashboard = """
        1:Add Receptionist
        2:Add Staff
        3:Exit
        """
        choice = None
        while choice != "3":
            choice = input(dashboard)
            if choice == "1":
                receptionist = Receptionist(self.appointments_schedules, len(self.employees) + 1)
                receptionist.register_receptionist()
                self.receptionists.append(receptionist)
                self.save_data("Receptionists.csv", self.receptionists,
                               ["Employee ID", "First Name", "Last Name", "Birthday"
                                   , "Phone Number", "Email", "Pay", "Hours Worked Week"
                                   , "Date Joined", "Experience"], "Receptionist")
            elif choice == "2":
                pass

    def doctor_dashboard(self):
        menu = """
        1:Issue Prescription
        2:Add availability
        3:Add appointment
        4:Show availability
        5:Exit
        """
        choice = None
        while choice != "5":
            choice = input(menu)
            doctor = input("Please enter full name of doctor: ")
            for d in self.doctors:
                if d.first_name + " " + d.last_name == doctor:
                    doctor = d
            if choice == "1":
                doctor.issue_prescription()
            elif choice == "2":
                doctor.add_availability()
                print(doctor.availabilities, "DD")
                self.save_data("Doctors.csv", self.doctors, ["Employee ID", "First Name", "Last Name", "Birthday"
                    , "Phone Number", "Email", "Pay", "Hours Worked Week"
                    , "Date Joined", "Experience", "Availability", "Appointments", "Prescriptions"],
                               "Doctor")
            elif choice == "3":
                appointment_id = len(self.appointments_schedules.appointments) + 1
                doctor.add_appointment(appointment_id, )
            elif choice == "4":
                doctor.show_availability()

    def nurse_dashboard(self):
        menu = """
        1:Add availability
        2:Add appointment
        3:Show availability
        4:Exit
        """
        choice = input(menu)
        while choice != "4":
            choice = input(menu)
            nurse = input("Please enter full name of Nurse: ")
            for d in self.nurses:
                if d.first_name + " " + d.last_name == nurse:
                    nurse = d
            if choice == "1":
                nurse.add_availability()
                self.save_data("Nurses.csv", self.nurses, ["Employee ID", "First Name", "Last Name", "Birthday"
                    , "Phone Number", "Email", "Pay", "Hours Worked Week"
                    , "Date Joined", "Experience", "Availability", "Appointments"], "Nurse")
            elif choice == "2":
                appointment_id = len(self.appointments_schedules) + 1
                nurse.add_appointment(appointment_id, )
            elif choice == "3":
                nurse.show_availability()

    def patient_dashboard(self):
        dashboard = """
        1:Add Patient
        2:Exit
        """
        choice = None
        while choice != "2":
            choice = input("Please enter option: " + dashboard)
            if choice == "1":
                patient = Patient(len(self.patients) + 1)
                patient.register_patient()
                self.patients.append(patient)
                self.save_data("Patients.csv", self.patients, ["Patient ID", "First Name", "Last Name", "Birthday"
                    , "Phone Number", "Email", "Address", "Prescription", "Prescriptions", "Appointment"], "Patient")
                print("patient has been added")

    def save_data(self, file_name, data_list, header, type):
        with open(file_name, "w") as file:
            csv_writer = writer(file)
            csv_writer.writerow(header)
            for entry in data_list:
                if type == "Doctor":
                    object = [entry.get_employee_number(), entry.first_name, entry.last_name, entry.birthday,
                              entry.get_phone_number(),
                              entry.get_email(), entry.get_pay_rate(), entry.get_hours_worked_week(),
                              entry.get_date_joined(),
                              entry.experience, entry.get_pay(), entry.availabilities,
                              entry.appointments, entry.prescriptions]
                elif type == "Nurse":
                    object = [entry.get_employee_number(), entry.first_name, entry.last_name, entry.birthday,
                              entry.get_phone_number(),
                              entry.get_email(), entry.get_pay_rate(), entry.get_hours_worked_week(),
                              entry.get_date_joined(),
                              entry.experience, entry.get_pay(),entry.availabilities,
                              entry.appointments]
                elif type == "Patient":
                    object = [entry.patient_id, entry.first_name, entry.last_name, entry.birthday,
                              entry.get_phone_number(),
                              entry.get_email(), entry.address, entry.prescription, entry.prescriptions,
                              entry.appointment]
                elif type == "Receptionist":
                    object = [entry.get_employee_number(), entry.first_name, entry.last_name, entry.birthday,
                              entry.get_phone_number(),
                              entry.get_email(), entry.get_pay_rate(), entry.get_hours_worked_week(),
                              entry.get_date_joined(), entry.experience, entry.get_pay()]
                csv_writer.writerow(object)

    def load_data(self, file_name, type):
        with open(file_name, "r") as file:
            csv_reader = reader(file)
            for entry in list(csv_reader)[1:]:
                if type == "Doctor":
                    object = Doctor(len(self.employees)+1)
                    object.set_employee_number(entry[0])
                    object.first_name = entry[1]
                    object.last_name = entry[2]
                    object.birthday = entry[3]
                    object.set_phone_number(entry[4])
                    object.set_email(entry[5])
                    object.set_pay_rate(entry[6])
                    object.set_hours_worked_week(entry[7])
                    object.set_date_joined(entry[8])
                    object.experience = entry[9]
                    object.set_pay(entry[10])
                    object.availabilities = entry[11]
                    object.appointments = entry[12]
                    object.prescriptions = entry[13]
                    self.doctors.append(object)
                elif type == "Nurse":
                    object = Nurse(len(self.employees)+1)
                    object.set_employee_number(entry[0])
                    object.first_name = entry[1]
                    object.last_name = entry[2]
                    object.birthday = entry[3]
                    object.set_phone_number(entry[4])
                    object.set_email(entry[5])
                    object.set_pay_rate(entry[6])
                    object.set_hours_worked_week(entry[7])
                    object.set_date_joined(entry[8])
                    object.experience = entry[9]
                    object.set_pay(entry[10])
                    object.availabilities = entry[11]
                    object.appointments = entry[12]
                    self.nurses.append(object)
                elif type == "Patient":
                    object = Patient(len(self.patients) + 1)
                    object.first_name = entry[0]
                    object.last_name = entry[1]
                    object.birthday = entry[2]
                    object.set_phone_number(entry[3])
                    object.set_email(entry[4])
                    object.address = entry[5]
                    object.prescription = entry[6]
                    object.prescriptions = entry[7]
                    object.appointment = entry[8]
                    self.patients.append(object)
                elif type == "Receptionist":
                    object = Receptionist(self.appointments_schedules, len(self.employees)+1)
                    object.set_employee_number(entry[0])
                    object.first_name = entry[1]
                    object.last_name = entry[2]
                    object.birthday = entry[3]
                    object.set_phone_number(entry[4])
                    object.set_email(entry[5])
                    object.set_pay_rate(entry[6])
                    object.set_hours_worked_week(entry[7])
                    object.set_date_joined(entry[8])
                    object.experience = entry[9]
                    object.set_pay(entry[10])
                    self.receptionists.append(object)
                    self.receptionist = self.receptionists[0]
