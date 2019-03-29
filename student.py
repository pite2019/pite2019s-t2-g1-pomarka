class Student:
    grades = {}

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        print(name + " " + surname + " added!")

class Course:
    def __init__(self, course_name, hours):
        self.course_name = course_name
        self.hours = hours
        print(course_name + " added as a course with " + str(hours) + " hours!")

class Scores:
    def __init__(self, grade_name, student, course, grade):
        self.grade_name = grade_name
        self.student = student
        self.course = course
        self.grade = grade
        print("Student " + student.name + " " + student.surname + " got " + str(grade) + " from " + grade_name + " in " + course.course_name)
        student.grades[course] = grade
        print("Grades of student " + student.surname + ": ")
        #sprint(student.grades.values())

class Attendace:
    def __init__(self, student, course):
        self.student = student
        self.course = course


s1 = Student("John", "Smith")
c1 = Course("Physics", 30)
test1 = Scores("Test 1", s1, c1, 5)
test2 = Scores("Test 2", s1, c1, 3)