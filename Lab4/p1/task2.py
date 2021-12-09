import re
import datetime


class Notebook:

    def __init__(self, name, surname, phone, birthday):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.birthday = birthday

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
    def phone(self):
        """Phone getter"""
        return self.__phone

    @phone.setter
    def phone(self, phone):
        """Phone setter"""
        if not isinstance(phone, str):
            raise TypeError("Wrong type of phone number!")
        check = re.compile("^[+]380\\d{9}$")
        if not check.match(phone):
            raise ValueError("Wrong input of phone number!")
        self.__phone = phone

    @property
    def birthday(self):
        """birthday getter"""
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        """birthday setter"""
        if not isinstance(birthday, str):
            raise TypeError("Wrong type of birthday!")
        if not datetime.datetime.strptime(birthday, "%d.%m.%Y"):
            raise ValueError("Wrong input of birthday!")
        self.__birthday = birthday

    def __str__(self):
        return f"{self.name} {self.surname}: " \
               f"Phone number - {self.phone} Birthday - {self.birthday}\n"


class ListOfPeople:

    def __init__(self, people=None):
        if people is None:
            people = []
        self.people = people

    @property
    def people(self):
        """people getter"""
        return self.__people

    @people.setter
    def people(self, people):
        """people setter"""
        if not isinstance(people, list):
            raise TypeError("Wrong type of people!")
        if not all(isinstance(person, Notebook) for person in people):
            raise ValueError("Wrong value of one of people!")
        self.__people = people

    def __add__(self, other):
        if isinstance(other, Notebook):
            add_list = self.people.copy()
            add_list.append(other)
            return ListOfPeople(add_list)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Notebook):
            if other not in self.people:
                raise ValueError("Person is not in list!")
            sub_list = self.people.copy()
            sub_list.remove(other)
            return ListOfPeople(sub_list)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, str):
            for person in self.people:
                if any(other == value for value in person.__dict__.values()):
                    find_list = [person]
                    return ListOfPeople(find_list)
        else:
            return NotImplemented

    def __str__(self):
        return f"{''.join(map(str, self.people))}"


if __name__ == "__main__":
    first = Notebook("Aaa", "Bbb", "+380980987777", "05.06.2005")
    second = Notebook("Ccc", "Ddd", "+380980989999", "01.02.2020")
    third = Notebook("Eee", "Fff", "+380980988888", "03.04.2020")
    print(first, second, sep='\n')
    our_notebook = ListOfPeople()

    plus = our_notebook + third
    plus_one = plus + first
    plus_two = plus_one + second
    print(plus_two)
    minus = plus_two - first
    print(minus)
    find_name = minus * "01.02.2020"
    print(find_name)
