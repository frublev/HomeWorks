class Universiter:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}

    def average_grade(self):
        sum_grades = 0
        count_grades = 0
        for grade in self.grades.values():
            sum_grades += sum(grade)
            count_grades += len(grade)
        return sum_grades / count_grades

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()


class Student(Universiter):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.average_grade()}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}\n"

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


# class Mentor(Universiters):
#     def __init__(self, name, surname):
#         super().__init__(name, surname)
#         self.courses_attached = []


class Lecturer(Universiter):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {self.average_grade()}\n"


class Reviewer(Universiter):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def av_grade_student(students_list, course):
    grades = 0
    count_grades = 0
    for student in students_list:
        if isinstance(student, Student) and course in student.courses_in_progress:
            grades += sum(student.grades[course])
            count_grades += len(student.grades[course])
        else:
            return 'Ошибка'
    return grades / count_grades


def av_grade_lecturer(lecturers_list, course):
    grades = 0
    count_grades = 0
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            grades += sum(lecturer.grades[course])
            count_grades += len(lecturer.grades[course])
        else:
            return 'Ошибка'
    return grades / count_grades


student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.courses_in_progress += ['English']
student1.finished_courses += ['Введение в програмирование']

student2 = Student('Susana', 'Caputova', 'female')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Git']
student2.courses_in_progress += ['English']
student2.finished_courses += ['PHP']

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Git']

lecturer2 = Lecturer('Igor', 'Matovic')
lecturer2.courses_attached += ['Git']
lecturer2.courses_attached += ['English']

reviewer1 = Reviewer('John', 'Dow')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('El', 'Batori')
reviewer2.courses_attached += ['English']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 7)

reviewer2.rate_hw(student1, 'English', 8)
reviewer2.rate_hw(student1, 'English', 7)
reviewer2.rate_hw(student1, 'English', 6)
reviewer2.rate_hw(student2, 'English', 10)
reviewer2.rate_hw(student2, 'English', 9)
reviewer2.rate_hw(student2, 'English', 8)

student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 8)
student1.rate_lecturer(lecturer1, 'Git', 10)
student1.rate_lecturer(lecturer1, 'Git', 9)
student1.rate_lecturer(lecturer1, 'Git', 8)
student1.rate_lecturer(lecturer2, 'English', 7)
student1.rate_lecturer(lecturer2, 'English', 6)
student1.rate_lecturer(lecturer2, 'English', 5)

student2.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer1, 'Python', 7)
student2.rate_lecturer(lecturer1, 'Python', 8)
student1.rate_lecturer(lecturer2, 'Git', 9)
student1.rate_lecturer(lecturer2, 'Git', 8)
student1.rate_lecturer(lecturer2, 'Git', 7)
student2.rate_lecturer(lecturer2, 'English', 10)
student2.rate_lecturer(lecturer2, 'English', 9)
student2.rate_lecturer(lecturer2, 'English', 8)

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print(student1)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(av_grade_student(students, 'English'))
print(av_grade_lecturer(lecturers, 'Git'))
print(lecturer1>lecturer2)