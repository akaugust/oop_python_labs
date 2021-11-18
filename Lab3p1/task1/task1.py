import json


class Events:
    """
    Class hat creates events(name, tickets` quantities and prices)
    """
    events_tickets = []
    advance_tickets = 0
    late_tickets = 0
    student_tickets = 0

    def __init__(self, filename, name, regular, advance, late, student, price):
        self.filename = filename
        self.name = name
        self.regular = regular
        self.advance = advance
        self.late = late
        self.student = student
        self.price = price
        self.advance_price = round(price * 0.6)
        self.late_price = round(price * 1.1)
        self.student_price = round(price * 0.5)
        self.quantity = regular + advance + late + student
        Events.add_event(self)

    def add_event(self):
        """Adds event`s dict to the file"""
        event = {
            "Filename": self.filename,
            "Name": self.name,
            "Regular quantity": self.regular,
            "Regular price": self.price,
            "Advance quantity": self.advance,
            "Advance price": self.advance_price,
            "Late quantity": self.late,
            "Late price": self.late_price,
            "Student quantity": self.student,
            "Student price": self.student_price
        }
        with open(self.filename, "w") as write_file:
            json.dump(event, write_file)
        write_file.close()

    @property
    def name(self):
        """Name getter"""
        return self.__name

    @name.setter
    def name(self, name):
        """Name setter"""
        if not isinstance(name, str):
            raise TypeError("Wrong type of name!")
        if not name:
            raise ValueError("Wrong value of name!")
        self.__name = name

    @property
    def price(self):
        """Price getter"""
        return self.__price

    @price.setter
    def price(self, price):
        """Price setter"""
        if not isinstance(price, int):
            raise TypeError("Wrong type of price!")
        if price <= 0:
            raise ValueError("Price can`t be 0 or lower!")
        self.__price = price

    @property
    def regular(self):
        """Regular type ticket quantity getter"""
        return self.__regular

    @regular.setter
    def regular(self, regular):
        """Regular type ticket quantity setter"""
        if not isinstance(regular, int):
            raise TypeError("Wrong type of regular tickets quantity!")
        if regular <= 0:
            raise ValueError("Regular quantity can`t be 0 or lower!")
        self.__regular = regular

    @property
    def advance(self):
        """Advance getter"""
        return self.__advance

    @advance.setter
    def advance(self, advance):
        """Advance type ticket quantity setter"""
        if not isinstance(advance, int):
            raise TypeError("Wrong type of advance tickets quantity!")
        if advance <= 0:
            raise ValueError("Advance quantity price can`t be 0 or lower!")
        self.__advance = advance

    @property
    def late(self):
        """Late type ticket quantity getter"""
        return self.__late

    @late.setter
    def late(self, late):
        """Late type ticket quantity setter"""
        if not isinstance(late, int):
            raise TypeError("Wrong type of late tickets quantity!")
        if late <= 0:
            raise ValueError("Late quantity can`t be 0 or lower!")
        self.__late = late

    @property
    def student(self):
        """Student type ticket quantity getter"""
        return self.__student

    @student.setter
    def student(self, student):
        """Student type ticket quantity setter"""
        if not isinstance(student, int):
            raise TypeError("Wrong type of student tickets quantity!")
        if student <= 0:
            raise ValueError("Student quantity can`t be 0 or lower!")
        self.__student = student

    def __str__(self):
        return f"Event: \n" \
               f"{self.__regular} regular tickets, price - {self.__price}, " \
               f"{self.__advance} advance tickets, price - {self.advance_price}, " \
               f"{self.__late} late tickets, price - {self.late_price}, " \
               f"{self.__student} student tickets, price - {self.student_price} \n"


class Tickets:
    """
    Class which creates regular tickets
    """
    file_tickets = []

    def __init__(self, event, number, days, price, ticket_type="Regular ticket"):
        self.event = event
        self.number = number
        self.days = days
        self.price = price
        self.ticket_type = ticket_type
        Tickets.add_ticket(self)
        if len(self.event.events_tickets) > event.quantity:
            raise ValueError("There are no more tickets!")

    def add_ticket(self):
        """Adds ticket to the tickets` file"""
        ticket = {
            "Event": self.event.name,
            "Number": self.number,
            "Type": self.ticket_type,
            "Days": self.days,
            "Price": self.price
        }
        self.file_tickets.append(ticket)
        with open("tickets_info.json", "w") as write_file:
            json.dump(self.file_tickets, write_file)
        write_file.close()

    @property
    def event(self):
        """Event getter"""
        return self.__event

    @event.setter
    def event(self, event):
        """Event setter"""
        if not isinstance(event, Events):
            raise TypeError("That is not an Event type!")
        self.__event = event

    @property
    def number(self):
        """Number type ticket quantity getter"""
        return self.__number

    @number.setter
    def number(self, number):
        """Number type ticket quantity setter"""
        if not isinstance(number, int):
            raise TypeError("Wrong type of number!")
        if number <= 0:
            raise ValueError("Number can`t be 0 or lower!")
        for ticket in self.event.events_tickets:
            if number in ticket.values():
                raise ValueError("This ticket already exists!")
        self.__number = number

    @property
    def days(self):
        """Days getter"""
        return self.__days

    @days.setter
    def days(self, days):
        """Days setter"""
        if not isinstance(days, int):
            raise TypeError("Wrong type of days!")
        if days <= 0:
            raise ValueError("Days can`t be 0 or lower!")
        self.__days = days

    @staticmethod
    def get_number(event, number):
        """Finds ticket by it`s number"""
        with open("tickets_info.json", "r") as read_file:
            info = json.load(read_file)
        for ticket in info:
            if ticket.get("Event") == event.name and ticket.get("Number") == number:
                return ticket

    @staticmethod
    def get_ticket_price(event, number):
        """Finds ticket`s price"""
        with open("tickets_info.json", "r") as read_file:
            info = json.load(read_file)
        for ticket in info:
            if ticket.get("Event") == event.name and ticket.get("Number") == number:
                return ticket.get("Price")

    @staticmethod
    def get_regular_price(filename):
        """Gets regular price of the ticket from event"""
        with open(filename, "r") as read_file:
            info = json.load(read_file)
        return info.get("Regular price")

    def __str__(self):
        return f"{self.ticket_type} ticket #{self.number} for the {self.event.name} event:" \
               f" price - {self.price}, bought {self.days} days before the event"


class AdvanceTicket(Tickets):
    """
    Class which creates advance tickets
    """
    def __init__(self, event, number, days):
        if days < 60:
            raise ValueError("This ticket can be purchased only 60 or more days before the event!")
        with open(event.filename, "r") as read_file:
            info = json.load(read_file)
        super().__init__(event, number, days, info.get("Advance price"), "Advance ticket")
        event.advance_tickets += 1
        if event.advance_tickets > event.advance:
            raise ValueError("There are no more advance tickets!")


class LateTicket(Tickets):
    """
    Class which creates late tickets
    """
    def __init__(self, event, number, days):
        if days > 10:
            raise ValueError("This ticket can be purchased only fewer than 10 days before the event!")
        with open(event.filename, "r") as read_file:
            info = json.load(read_file)
        super().__init__(event, number, days, info.get("Late price"), "Late ticket")
        event.late_tickets += 1
        if event.late_tickets > event.late:
            raise ValueError("There are no more late tickets!")


class StudentTicket(Tickets):
    """
    Class which creates student tickets
    """
    def __init__(self, event, number, days):
        with open(event.filename, "r") as read_file:
            info = json.load(read_file)
        super().__init__(event, number, days, info.get("Student price"), "Student ticket")
        event.student_tickets += 1
        if event.student_tickets > event.student:
            raise ValueError("There are no more student tickets!")


if __name__ == '__main__':
    e1 = Events("python.json", "Python", 1, 2, 1, 3, 100)
    print(e1)

    buy_ticket1 = Tickets(e1, 1, 15, Tickets.get_regular_price(e1.filename))
    buy_ticket2 = AdvanceTicket(e1, 2, 61)
    buy_ticket3 = AdvanceTicket(e1, 3, 70)
    buy_ticket4 = LateTicket(e1, 4, 2)
    buy_ticket5 = StudentTicket(e1, 5, 10)
    buy_ticket6 = StudentTicket(e1, 6, 48)
    buy_ticket7 = StudentTicket(e1, 7, 14)
    print(buy_ticket1, buy_ticket2, buy_ticket3, buy_ticket4, buy_ticket5, buy_ticket6, buy_ticket7, sep='\n')

    # e2 = Events("java.json", "Java", 1, 1, 1, 1, 75)
    # buy_ticket8 = Tickets(e2, 1, 15, Tickets.get_regular_price(e2.filename))
    # buy_ticket9 = AdvanceTicket(e2, 2, 61)
    # buy_ticket10 = LateTicket(e2, 3, 2)
    # buy_ticket11 = StudentTicket(e2, 4, 10)
    # print('', buy_ticket8, buy_ticket9, buy_ticket10, buy_ticket11, sep='\n')

    print(Tickets.get_number(e1, 7))
    print(Tickets.get_ticket_price(e1, 3))
