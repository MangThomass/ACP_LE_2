class Student: #parent class to represent a student
    def __init__(self,student_id,Student_name,email, grades, courses): # constructor to initialize student attributes
        self.id_name = (student_id, Student_name) #tuple of id and name
        self.email = email # String of email
        self.grades = grades if grades else {} #dictionary of grades
        self.courses = courses if courses else set() #set of courses

    def __str__(self): #String representation of student
           return (
        f"Student Information:\n"
        f"  ID     : {self.id_name[0]}\n"
        f"  Name   : {self.id_name[1]}\n"
        f"  Email  : {self.email}\n"
        f"  Grades : {self.grades}\n"
        f"  Courses: {self.courses}\n"
        "-------------------------\n"
        ""
    )
    
class studentRecords(Student): #subclass of student that inherits from Student class

    def __init__(self): # Initialize studentRecords attributes
        self.students = [] #creates an empty list to store student instances

    # Add a new student to the records
    def add_student(self, student_id,Student_name, email=None, grades=None, courses=None):
        new_student = Student(student_id,Student_name, email, grades, courses) # Create new student instance
        self.students.append(new_student) # Add this student to list
        return "student added successfully" #confirmation message
    
    #update student details based on student ID
    def update_student(self, student_id,Student_name, email=None, grades=None, courses=None):
        for student in self.students:
            if student.id_name[0] == student_id: # Find student by ID
                if email:
                    student.email = email # Update email if provided
                if grades:
                    student.grades = grades # Update grades if provided
                if courses: 
                    student.courses = courses # Update courses if provided
                return "student updated successfully" #confirmation message
        return "student not found" # if no matching ID found 
    
    #delete student based on student ID
    def delete_student(self, student_id):
        for student in self.students: # go through student list
            if student.id_name[0] == student_id: # Find student by ID
                self.students.remove(student) # Remove student from the list
                return "student deleted successfully" #confirmation message
        return "student not found" # if no matching ID found
    
    #display all students in the records
    def display_students(self):
        if not self.students: #if the student list is empty
            return "No students available" #show this message
        return "\n".join(str(student) for student in self.students) #converts each student to string and joins them with newline
    

    #enroll a student in a course based on student ID
    def enroll_course(self, student_id, course):
        for student in self.students: # go through student list
            if student.id_name[0] == student_id: # Find student by ID
                if student.courses is None:
                    student.courses = [] #if no courses exist, initialize an empty list
                student.courses.add(course) # Add the course to the student's set of courses
                return "course enrolled successfully" #confirmation message
        return "student not found" # if no matching ID found
    
    #search for a student by ID and return their details
    def search_student(self, student_id):
        for student in self.students: # go through student list
            if student.id_name[0] == student_id: # Find student by ID
                return str(student) # Return student details as string
        return "student not found" # if no matching ID found
    

#--- Example usage ---
records = studentRecords() # Create an instance of studentRecords
print(records.add_student(1, "Alice", "alice@gmail")) #add the student "Alice"
print(records.add_student(2, "Bob", "bob@gmail")) #add the student "Bob"
print(records.display_students()) #display all students
print(records.search_student(1)) #search for student with ID 1 which is Alice
print(records.enroll_course(1, "Math")) #enroll Alice in Math course
print(records.update_student(1, "Alice", "alice_new@gmail", {"Math": "A"}, {"Math"})) #update Alice's email, grades and courses
print(records.delete_student(2)) #delete student with ID 2 which is Bob
print(records.display_students()) #display all students
