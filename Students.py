class Student:
    def __init__(self, id_name,email, grades, courses):
        self.id_name = id_name
        self.email = email
        self.grades = grades
        self.courses = courses

        def __str__(self):
            return f"Student ID: {self.id_name}, Email: {self.email}, Grades: {self.grades}, Courses: {self.courses}"
    
class student_record(Student):

    def __init__(self):
        self.Class_list = []

    @classmethod
    def add_student(cls, id_name, email=None, grades=None, courses=None):
        new_student = cls(id_name, email, grades, courses) # Create new student instance
        cls.Class_list.append(new_student) # Add to class list
        return "student added successfully"
    
    @classmethod
    def update_student(cls, id_name, email=None, grades=None, courses=None):
        for student in cls.Class_list:
            if student.id_name == id_name: # Find student by ID
                if email:
                    student.email = email # Update email if provided
                if grades:
                    student.grades = grades # Update grades if provided
                if courses: 
                    student.courses = courses # Update courses if provided
                return "student updated successfully"
        return "student not found"
    
    @classmethod
    def delete_student(cls, id_name):
        for student in cls.Class_list: # Iterate through class list
            if student.id_name == id_name: # Find student by ID
                cls.Class_list.remove(student) # Remove student from class list
                return "student deleted successfully"
        return "student not found"
    
    @classmethod
    def display_students(cls):
        if not cls.Class_list:
            return "No students available"
        return "\n".join(str(student) for student in cls.Class_list)
