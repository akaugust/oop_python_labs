class Student:
    """
    Class contains the student's name, surname, record book number and grades
    """

    all_book_numbers = []

    def __init__(self, name, surname, number, **kwargs):
        self.name = name
        self.surname = surname
        self.book_number = number
        self.grades = kwargs

    @property
    def name(self):
        """Name getter"""
        return self.__name

    @name.setter
    def name(self, name):
        """Name setter"""
        if not isinstance(name, str):
            raise TypeError("Wrong type of name!")
        if not name or name.__contains__(" "):
            raise ValueError("Wrong value of name!")
        self.__name = name

    @property
    def surname(self):
        """Surname getter"""
        return self.__surname

    @surname.setter
    def surname(self, surname):
        """Surname setter"""
        if not isinstance(surname, str):
            raise TypeError("Wrong type of surname!")
        if not surname or surname.__contains__(" "):
            raise ValueError("Wrong value of surname!")
        self.__surname = surname

    @property
    def book_number(self):
        """Book_number getter"""
        return self.__book_number

    @book_number.setter
    def book_number(self, number):
        if not isinstance(number, int):
            raise TypeError("Record book number can be only integer!")
        if number <= 0:
            raise ValueError("This is not a record book number")
        if number in self.all_book_numbers:
            raise ValueError("This record book number already exists!")
        self.all_book_numbers.append(number)
        self.__book_number = number

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        if not isinstance(grades, dict):
            raise TypeError("Wrong grades type!")
        if not grades:
            raise ValueError("There are no grades!")
        if not all(isinstance(values, int) for values in grades.values()):
            raise TypeError("Incorrect values type")
        if not all(0 <= values <= 100 for values in grades.values()):
            raise ValueError("Grade must be between 0 and 100!")
        self.__grades = grades

    def get_average_score(self):
        return sum(self.__grades.values()) / len(self.__grades.values())

    def __str__(self):
        return f"Student #{self.__book_number}: {self.__name} " \
               f"{self.__surname}\nGrades - {self.__grades}\n"


class Group:
    """
    The class contains a sequence of instances of the class Student
    """

    counter = 0
    same_students = []

    def __init__(self, *student):
        self.student = student
        for st in self.student:
            if st.name + st.surname in self.same_students:
                raise ValueError("There can`t be same students!")
            self.same_students.append(st.name + st.surname)
        self.counter += 1
        if self.counter > 20:
            raise ValueError("There can`t be more than 20 students")

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, student):
        if any(not isinstance(person, Student) for person in student):
            raise TypeError("That is not a Student type!")
        self.__student = list(student)

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("That is not a Product type!")
        self.student.append(student)
        self.counter += 1
        if self.counter > 20:
            raise ValueError("You can`t add more than 20 students")

    def del_product(self, student):
        if not isinstance(student, Student):
            raise TypeError("That is not a Product type!")
        if student in self.student:
            self.student.remove(student)
        else:
            raise NameError("This student doesn`t exist!")
        self.counter -= 1

    def five_best_students(self):
        average_score = {}
        for person in self.student:
            average_score[person.name] = person.get_average_score()
        sorted_average_score = {k: v for k, v in sorted(average_score.items(), key=lambda item: item[1], reverse=True)}
        return list(sorted_average_score.items())[0:5]

    def __str__(self):
        list_students = '\n'.join(list(map(str, self.student)))
        return f"Students: \n{list_students}\n"


if __name__ == '__main__':
    first = Student("Anne", "Kolly", 1, programming=100, math=90)
    second = Student("Kate", "McCoy", 2, programming=99, math=46)
    third = Student("Josh", "Chosty", 3, programming=56, math=28)
    forth = Student("Maria", "Forest", 4, programming=75, math=99)
    fifth = Student("Kelly", "Foxline", 5, programming=84, math=83)
    sixth = Student("Ron", "Stuward", 6, programming=23, math=15)
    print(first.get_average_score())
    student_group = Group(first, second, third, forth, fifth)
    print(student_group)
    student_group.add_student(sixth)
    print(student_group)
    print(student_group.five_best_students())
