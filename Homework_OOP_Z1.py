class Mentor:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Ментор: {self.name} {self.surname}"


class Lecturer(Mentor):

    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)


class Reviewer(Mentor):

    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)


def main():

    lecturer = Lecturer('Иван', 'Иванов')
    reviewer = Reviewer('Пётр', 'Петров')


    print(isinstance(lecturer, Mentor))
    print(isinstance(reviewer, Mentor))


    print(lecturer.courses_attached)
    print(reviewer.courses_attached)

if __name__ == "__main__":
    main()