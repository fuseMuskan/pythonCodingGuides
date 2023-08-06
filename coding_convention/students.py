import json


class StudentManagementSystem:
    def load_records(self):
        try:
            with open("./data/students.json", "r") as file:
                records = json.load(file)
        except FileNotFoundError:
            records = []
        return records

    def save_records(self, records):
        with open("./data/students.json", "w") as file:
            json.dump(records, file, indent=4)

    def add_student(self, student_id: str, name: str, age: int, grade: float):
        records = self.load_records()
        records.append({"student_id": student_id,
                        "name": name,
                        "age": age,
                        "grade": grade})
        self.save_records(records)
        print("Student record added successfully.")

    def search_student(self, identifier):
        records = self.load_records()
        for student in records:
            if (student["student_id"] == identifier or
                    student["name"].lower() == identifier.lower()):
                return student
            return None

    def update_student(self, identifier, field, new_value):
        records = self.load_records()
        for student in records:
            if (student["student_id"] == str(identifier) or
                    student["name"].lower() == identifier.lower()):
                student[field] = new_value
                self.save_records(records)
                print("Student information updated successfully.")
                return True
        return False


student_management_systemt = StudentManagementSystem()


#  Main Function
if __name__ == "__main__":
    while True:
        print("\nStudent Records Management System")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student Information")
        print("4. Quit")

        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = float(input("Enter Grade: "))
            student_management_systemt.add_student(
                student_id, name, age, grade)
        elif choice == 2:
            identifier = input("Enter Student ID or Name to search: ")
            result = student_management_systemt.search_student(identifier)
            if result:
                print("Student found:")
                print(f"{result['name']}, {result['age']}, {result['grade']}")
            else:
                print("Student not found.")
        elif choice == 3:
            identifier = input("Enter Student ID or Name to update: ")
            field = input("Enter field to update (age or grade): ")
            if field == "age":
                new_value = int(input("Enter new value: "))
            else:
                new_value = float(input("Enter new value: "))

            if student_management_systemt.update_student(
                    identifier, field, new_value):
                print("Student information updated successfully.")
            else:
                print("Student not found.")
        elif choice == 4:
            print("Exiting Student Records Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
