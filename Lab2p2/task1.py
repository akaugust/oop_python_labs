import re


class Customer:
    """
    Class with Customer`s info(name, surname, patronymic, phone)
    """

    def __init__(self, name, surname,
                 patronymic, phone):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.phone = phone

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
    def patronymic(self):
        """Patronymic getter"""
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        """Patronymic setter"""
        if not isinstance(patronymic, str):
            raise TypeError("Wrong type of patronymic!")
        if not patronymic or patronymic.__contains__(" "):
            raise ValueError("Wrong value of patronymic!")
        self.__patronymic = patronymic

    @property
    def phone(self):
        """Phone getter"""
        return self.__phone

    @phone.setter
    def phone(self, phone):
        """Phone setter"""
        if not isinstance(phone, str):
            raise TypeError("Wrong type of phone number!")
        check = re.match("^[+]380\\d{2}\\d{3}\\d{2}\\d{2}$", phone)
        if not check:
            raise ValueError("Wrong input of phone number!")
        self.__phone = phone

    def __str__(self):
        return f"{self.__surname} {self.__name} {self.__patronymic} - {self.__phone}"


class Product:
    """
    Class with Product`s info(price, description, dimensions)
    """

    def __init__(self, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions

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
    def description(self):
        """Description getter"""
        return self.__description

    @description.setter
    def description(self, description):
        """Description setter"""
        if not isinstance(description, str):
            raise TypeError("Wrong type of description!")
        if not description:
            raise ValueError("Wrong input of description!")
        self.__description = description

    @property
    def dimensions(self):
        """Dimensions getter"""
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Dimensions setter"""
        if not isinstance(dimensions, int):
            raise TypeError("Wrong type of dimensions!")
        if dimensions <= 0:
            raise ValueError("Dimensions can`t be negative or zero!")
        self.__dimensions = dimensions

    def __str__(self):
        return f"{self.__price} grivnas, {self.__description}, size: {self.__dimensions}"


class Order:
    """
    Class with Order info(customer, product)
    that calculates total value of ordered products
    """

    def __init__(self, customer, *products):
        self.customer = customer
        self.products = products

    @property
    def customer(self):
        """Customer getter"""
        return self.__customer

    @customer.setter
    def customer(self, customer):
        """Customer getter"""
        if not isinstance(customer, Customer):
            raise TypeError("That is not a Customer Type!")
        self.__customer = customer

    @property
    def products(self):
        """Product getter"""
        return self.__products

    @products.setter
    def products(self, products):
        """Customer setter"""
        if any(not isinstance(product, Product) for product in products):
            raise TypeError("That is not a Product type!")
        self.__products = list(products)

    def total_value(self):
        """Counts total value of products"""
        value = 0
        for element in self.products:
            value += element.price
        return value

    def add_product(self, product):
        """Adds products"""
        if not isinstance(product, Product):
            raise TypeError("That is not a Product type!")
        self.products.append(product)

    def del_product(self, product):
        """Deletes product"""
        if not isinstance(product, Product):
            raise TypeError("That is not a Product type!")
        if product in self.products:
            self.products.remove(product)
        else:
            raise NameError("This product doesn`t exist in order!")

    def __str__(self):
        product_list = '\n'.join(list(map(str, self.products)))
        return f"Customer [{self.customer}] ordered:\n{product_list}"


if __name__ == "__main__":

    a = Customer("Vika", "Yevtush", "Pavlivna", "+380987654321")
    b = Customer("Anonymous", "Anonymous", "Anonymous", "+380000000000")

    hat = Product(70, "Bershka hat", 25)
    gloves = Product(120, "Zara gloves", 34)
    dress = Product(500, "Dolce Gabbana dress", 46)
    shirt = Product(300, "Lois Vuitton shirt", 54)

    first = Order(a, hat, dress, gloves)
    second = Order(b, shirt, hat)

    print(first)
    print(second)

    new_shirt = Product(600, "Lois Vuitton new more expensive shirt", 54)
    second.add_product(new_shirt)
    print(second)

    second.del_product(shirt)
    print(second)
