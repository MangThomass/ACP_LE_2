class Student:
    def __init__(self,student_id,Student_name,email, grades, courses):
        self.id_name = (student_id, Student_name)
        self.email = email
        self.grades = grades if grades else {}
        self.courses = courses if courses else set()

    def __str__(self):
            return f"Student ID: {self.id_name[0]}, Name: {self.id_name[1]} Email: {self.email}, Grades: {self.grades}, Courses: {self.courses}"
    
class studentRecords(Student):

    def __init__(self):
        self.students = []

    def add_student(self, student_id,Student_name, email=None, grades=None, courses=None):
        new_student = Student(student_id,Student_name, email, grades, courses) # Create new student instance
        self.students.append(new_student) # Add to class list
        return "student added successfully"
    
    def update_student(self, student_id,Student_name, email=None, grades=None, courses=None):
        for student in self.students:
            if student.id_name[0] == student_id: # Find student by ID
                if email:
                    student.email = email # Update email if provided
                if grades:
                    student.grades = grades # Update grades if provided
                if courses: 
                    student.courses = courses # Update courses if provided
                return "student updated successfully"
        return "student not found"
    
    def delete_student(self, student_id):
        for student in self.students: # Iterate through class list
            if student.id_name[0] == student_id: # Find student by ID
                self.students.remove(student) # Remove student from class list
                return "student deleted successfully"
        return "student not found"
    
    def display_students(self):
        if not self.students:
            return "No students available"
        return "\n".join(str(student) for student in self.students)
    
    def enroll_course(self, student_id, course):
        for student in self.students:
            if student.id_name[0] == student_id:
                if student.courses is None:
                    student.courses = []
                student.courses.add(course)
                return "course enrolled successfully"
        return "student not found"
    
    def search_student(self, student_id):
        for student in self.students:
            if student.id_name[0] == student_id:
                return str(student)
        return "student not found"
    
records = studentRecords()
print(records.add_student(1, "Alice", "alice@gmail"))
print(records.add_student(2, "Bob", "bob@gmail"))
print(records.display_students())
print(records.search_student(1))
print(records.enroll_course(1, "Math"))
print(records.update_student(1, "Alice", "alice_new@gmail", {"Math": "A"}, {"Math"}))
print(records.display_students())
print(records.delete_student(2))
print(records.display_students())
