import json
from typing import List, Dict, Optional


class Student:
    def __init__(self, name, surname):
        self.student_diary = {}
        self.name = name
        self.surname = surname
        self.courses = { 'Math': {'scores': [], 'attendance': 0},
                         'English': {'scores': [], 'attendance': 0},
                         'History': {'scores': [], 'attendance': 0}}
        self.student_diary.update({'{} {}'.format(name, surname) : self.courses })

    def total_average_all_classes(self) -> float:
        sum_of_scores = sum(sum(course_details['scores']) for course_name, course_details in self.courses.items())
        number_of_scores = sum(len(course_details['scores']) for course_name, course_details in self.courses.items())
        avg = sum_of_scores / float(number_of_scores)
        return avg

    def total_average_one_class(self, class_name: str) -> float:
        sum_of_scores = sum(sum(course_details['scores'])
                            for course_name, course_details in self.courses.items()
                            if class_name == course_name)

        number_of_scores = sum(len(course_details['scores'])
                               for course_name, course_details in self.courses.items()
                               if class_name == course_name)

        avg = sum_of_scores / float(number_of_scores)
        return avg

    def total_attendance(self) -> int:
        return sum(course_details['attendance'] for course_name, course_details in self.courses.items())

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return str(self)

class Classroom:
    def __init__(self, classroom_name):
        self.classroom_name = classroom_name
        self.students: List[Student] = []
    
    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        return f"{self.classroom_name}: {self.students}"

    def __repr__(self):
        return str(self)

    def get_student(self, student_full_name: str) -> Optional[Student]:
        return next(filter(lambda s: f"{s.name} {s.surname}" == student_full_name, (s for s in self.students)), None)

def get_classrooms(data: Dict) -> Dict[str, Classroom]:
    classrooms = {}
    for class_name, students in data.items():
        classroom = Classroom(class_name)
        for student_fullname, courses in students.items():
            name, surname = student_fullname.split(" ")
            student = Student(name, surname)
            student.courses = courses
            classroom.add_student(student)
        classrooms[class_name] = classroom

    return classrooms

if __name__ == "__main__":

    with open('data.json', 'r') as f:
        data = json.loads(f.read())

    print('Students in class A:')
    for stud in data['A']:
        print(stud)
    print('\n')

    print('Students in class B:')
    for stud in data['B']:
        print(stud)
    print('\n')

    print('Students in class C:')
    for stud in data['C']:
        print(stud)
    print('\n')
    
    classrooms = get_classrooms(data)

    m = classrooms['A'].get_student("Maria Pomarańska")
    print(f'(A) Student`s Maria Pomarańska total average: {m.total_average_all_classes()}')

    k = classrooms['B'].get_student("Katy Perry")
    print(f'(B) Student`s Katy Perry total average: {k.total_average_all_classes()}')

    r = classrooms['C'].get_student("Ron Weasly")
    print(f'(C) Student`s Ron Weasly total average: {r.total_average_all_classes()}')
    print('\n')

    print(f'(A) Student`s Maria Pomarańska total attendance: {m.total_attendance()}')
    print(f'(B) Student`s Katy Perry total attendance: {k.total_attendance()}')
    print(f'(C) Student`s Ron Weasly total attendance: {r.total_attendance()}')
    print('\n')

    m1 = m.total_average_one_class('Math')
    print(f'(A) Student`s Maria Pomarańska Math average: {m1}')

    k2 = m.total_average_one_class('History')
    print(f'(B) Student`s Katy Perry History average: {k2}')

    r2 = m.total_average_one_class('English')
    print(f'(C) Student`s Ron Weasly English average: {r2}')