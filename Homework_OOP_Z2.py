class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    def __init__(self, first_name: str, last_name: str, gender: str):
        super().__init__(first_name, last_name)
        self.gender = gender
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer: 'Lecturer', course: str, grade: int):

        if not isinstance(lecturer, Lecturer):
            return "Ошибка"

        if course not in self.courses_in_progress:
            return "Ошибка"

        if course not in lecturer.courses_attached:
            return "Ошибка"

        if not (1 <= grade <= 10):
            return "Ошибка"

        if course not in lecturer.grades:
            lecturer.grades[course] = []
        lecturer.grades[course].append(grade)
        return None


class Lecturer(Person):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.courses_attached = []
        self.grades = {}


class Reviewer(Person):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.courses_attached = []

    def rate_hw(self, student: Student, course: str, grade: int):
        if not isinstance(student, Student):
            return "Ошибка"

        if course not in self.courses_attached:
            return f"Ошибка: преподаватель не прикреплен к курсу {course}"

        if course not in student.courses_in_progress:
            return f"Ошибка: студент не обучается на курсе {course}"

        if course not in student.grades:
            student.grades[course] = []
        student.grades[course].append(grade)


# Тестирование
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))    # Ошибка
print(student.rate_lecture(lecturer, 'C++', 8))     # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка

print(lecturer.grades)  # {'Python': [7]}

