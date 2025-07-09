class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Reviewer(Person):
    def __str__(self):
        return super().__str__()


class Lecturer(Person):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.lecture_grades = []  # Исправлено инициализацию списка

    @property
    def average_lecture_grade(self):
        return sum(self.lecture_grades) / len(self.lecture_grades) if self.lecture_grades else 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_lecture_grade:.1f}")

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_lecture_grade == other.average_lecture_grade

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_lecture_grade < other.average_lecture_grade

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_lecture_grade > other.average_lecture_grade


class Student(Person):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.grades = []  # Исправлено инициализацию списка
        self.courses_in_progress = []
        self.finished_courses = []

    @property
    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grade:.1f}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade == other.average_grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade < other.average_grade

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade > other.average_grade


# Пример использования
if __name__ == "__main__":
    # Создаем объекты
    reviewer = Reviewer("Some", "Buddy")
    lecturer = Lecturer("Some", "Buddy")
    lecturer.lecture_grades = [9, 10, 9, 10]  # Исправлено добавление оценок

    student = Student("Ruoy", "Eman")
    student.grades = [9, 10, 9, 10]  # Исправлено добавление оценок
    student.courses_in_progress = ["Python", "Git"]
    student.finished_courses = ["Введение в программирование"]

    # Проверяем вывод
    print("Рецензент:")
    print(reviewer)
    print("\nЛектор:")
    print(lecturer)
    print("\nСтудент:")
    print(student)

    # Проверяем сравнение
    print("\nСравнение лекторов и студентов:")
    print(f"Лектор > Студент: {lecturer > student}")
    print(f"Лектор < Студент: {lecturer < student}")
    print(f"Лектор == Студент: {lecturer == student}")
