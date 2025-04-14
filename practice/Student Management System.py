import json

class Student:
    def __init__(self, name, roll_no, section, clss):
        self.name = name
        self.roll_no = roll_no
        self.section = section
        self.clss = clss
    
    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.roll_no}, Section: {self.section}, Class: {self.clss}"
        
    def to_dict(self):
        return {
            "name": self.name,
            "roll_no": self.roll_no,
            "section": self.section,
            "class": self.clss
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["roll_no"], data["section"], data["class"])


class Attendance:
    def __init__(self, date, roll_no, status):
        self.date = date
        self.roll_no = roll_no
        self.status = status

    def __str__(self):
        return f"Date: {self.date}, Roll No: {self.roll_no}, Status: {self.status}"
    
    def to_dict(self):
        return {
            "date": self.date,
            "roll_no": self.roll_no,
            "status": self.status
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(data["date"], data["roll_no"], data["status"])


class Marks:
    def __init__(self, subject, marks):
        self.subject = subject 
        self.marks = marks

    def __str__(self):
        return f"Subject: {self.subject}, Marks: {self.marks}"
    
    def to_dict(self):
        return {
            "subject": self.subject,
            "marks": self.marks
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(data["subject"], data["marks"])


class SchoolManagementSystem:
    def __init__(self):
        self.Students = []
        self.Attendance = []
        self.Marks = []
        self.load_data()
    
    def save_data(self):
        with open("Students.json", "w") as file:
            json.dump([student.to_dict() for student in self.Students], file, indent=4)
            
        with open("Attendance.json", "w") as file:
            json.dump([att.to_dict() for att in self.Attendance], file, indent=4)
            
        with open("Marks.json", "w") as file:
            json.dump([mark.to_dict() for mark in self.Marks], file, indent=4)
    
    def load_data(self):
        try:
            with open("Students.json", "r") as file:
                data = json.load(file)
                self.Students = [Student.from_dict(d) for d in data]
        except:
            self.Students = []

        try:
            with open("Attendance.json", "r") as file:
                data = json.load(file)
                self.Attendance = [Attendance.from_dict(d) for d in data]
        except:
            self.Attendance = []

        try:
            with open("Marks.json", "r") as file:
                data = json.load(file)
                self.Marks = [Marks.from_dict(d) for d in data]
        except:
            self.Marks = []
        
    def add_student(self):
        name = input("Enter student name: ")
        roll_no = input("Enter student roll number: ")
        section = input("Enter student section: ")
        clss = input("Enter student class: ")

        for student in self.Students:
            if student.roll_no == roll_no:
                print("Student already exists!")
                return
            
        Std = Student(name, roll_no, section, clss)
        self.Students.append(Std)
    #-----------------------------------------------------
        Date = input("Enter date (YYYY-MM-DD): ")
        Status = input("Enter attendance status (Present/Absent): ")
        Atd = Attendance(Date, roll_no, Status) 
        self.Attendance.append(Atd)
    #----------------------------------------------------
        subject = input("Enter subject name: ")
        marks = int(input("Enter marks: "))

        Std_Marks = Marks(subject, marks)
        self.Marks.append(Std_Marks)
    #-----------------------------------------------------
        self.save_data()
        print("Student added successfully!") 

    def delete_student(self):
        roll_no = int(input("Enter student roll no to delete: "))
        for student in self.Students:
            if student.roll_no == roll_no:
                self.Students.remove(student)
                self.Attendance.remove(student)

                self.save_data()
                print("Student deleted successfully!")
                return
            else:
                print("Student not found!")
                break

    def view_students(self):
        if not self.Students:
            print("No students found!")
        else:
            for student in self.Students:
                print(student)
        
def main():
    while(True):
        objecto = SchoolManagementSystem()

        print("Welcome to the Student Management System")

        print("1- Add Student")
        print("2- Delete Student")
        print("3- View Students")
        print("4- Exit")

        choice = int(input("Enter your choice: "))
        try:
            if choice == 1 : 
               objecto.add_student()
            elif choice == 2:
                objecto.delete_student()
            elif choice == 3:
                objecto.view_students()
            elif choice == 4:
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Try again later.")

        except ValueError:
            print("Invalid input. Please enter a number.")
        except TypeError: 
            print("Invalid type. Please enter a valid input.")
        except Exception as e:
            print(f"An error occurred: {e}")

main()
