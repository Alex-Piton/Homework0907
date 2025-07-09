class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.homework_grades = {}  # {course: [grades]}

    def add_homework_grade(self, course, grade):
        if course not in self.homework_grades:
            self.homework_grades[course] = []
        self.homework_grades[course].append(grade)

    def get_average_homework_grade(self, course):
        if course in self.homework_grades:
            return sum(self.homework_grades[course]) / len(self.homework_grades[course])
        return 0

    def __str__(self):
        return f"Студент {self.name} (ID: {self.student_id}), курс: {self.course}"


class Lecturer:
    def __init__(self, lecturer_id, name, course):
        self.lecturer_id = lecturer_id
        self.name = name
        self.course = course
        self.lecture_grades = {}  # {course: [grades]}

    def add_lecture_grade(self, course, grade):
        if course not in self.lecture_grades:
            self.lecture_grades[course] = []
        self.lecture_grades[course].append(grade)

    def get_average_lecture_grade(self, course):
        if course in self.lecture_grades:
            return sum(self.lecture_grades[course]) / len(self.lecture_grades[course])
        return 0

    def __str__(self):
        return f"Лектор {self.name} (ID: {self.lecturer_id}), курс: {self.course}"


def calculate_average_student_grade(students, course):
    total_grades = 0
    count = 0
    for student in students:
        if course in student.homework_grades:
            total_grades += sum(student.homework_grades[course])
            count += len(student.homework_grades[course])
    return total_grades / count if count != 0 else 0


def calculate_average_lecturer_grade(lecturers, course):
    total_grades = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.lecture_grades:
            total_grades += sum(lecturer.lecture_grades[course])
            count += len(lecturer.lecture_grades[course])
    return total_grades / count if count != 0 else 0


student1 = Student(1, "Иван Петров", "Python-разработчик")
student2 = Student(2, "Анна Сидорова", "Python-разработчик")

lecturer1 = Lecturer(101, "Петр Иванов", "Python-разработчик")
lecturer2 = Lecturer(102, "Мария Смирнова", "Python-разработчик")

student1.add_homework_grade("Python-разработчик", 4)
student1.add_homework_grade("Python-разработчик", 5)
student2.add_homework_grade("Python-разработчик", 5)
student2.add_homework_grade("Python-разработчик", 4)

lecturer1.add_lecture_grade("Python-разработчик", 5)
lecturer1.add_lecture_grade("Python-разработчик", 5)
lecturer2.add_lecture_grade("Python-разработчик", 4)
lecturer2.add_lecture_grade("Python-разработчик", 5)

print("Студенты:")
print(student1)
print(f"Средняя оценка за домашние задания: {student1.get_average_homework_grade('Python-разработчик')}")
print(student2)
print(f"Средняя оценка за домашние задания: {student2.get_average_homework_grade('Python-разработчик')}")