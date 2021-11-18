import json


class Pizza:
    """
    Class which creates regular pizza
    """
    all_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    all_pizzas = []

    def __init__(self, name, price, ingredients, day):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.day = day
        Pizza.add_pizza(self)

    def add_pizza(self):
        """Adds pizza to the pizzas` file"""
        pizza = {
            "Day": self.day,
            "Name": self.name,
            "Price": self.price,
            "Ingredients": self.ingredients
        }
        self.all_pizzas.append(pizza)
        with open("pizzas_of_the_day.json", "w") as write_file:
            json.dump(self.all_pizzas, write_file)
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
        if not name or name.__contains__(" "):
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
    def ingredients(self):
        """Ingredients setter"""
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        """Ingredients getter"""
        if any(not isinstance(ingredient, str) for ingredient in ingredients):
            raise TypeError("Wrong type of ingredients")
        with open("ingredients.json", "r") as read_file:
            ingredients_data = json.load(read_file)
        for ingredient in ingredients:
            if ingredient not in ingredients_data:
                raise ValueError("This ingredient does not exhist!")
        self.__ingredients = ingredients

    @property
    def day(self):
        """Day getter"""
        return self.__day

    @day.setter
    def day(self, day):
        """Day setter"""
        if not isinstance(day, str):
            raise TypeError("Wrong type of day!")
        if not day or day.__contains__(" "):
            raise ValueError("Wrong value of day!")
        if day not in self.all_days:
            raise ValueError("This day doesn`t exist!")
        self.__day = day

    @staticmethod
    def add_all_ingredients(*ingredients):
        """Function adding possible additional ingredients"""
        all_ingredients = []
        for ingredient in ingredients:
            if any(not isinstance(ingredient, str) for ingredient in ingredients):
                raise TypeError("Wrong type of ingredients")
            if ingredient in all_ingredients:
                raise ValueError("This ingredient is already on the list!")
            all_ingredients.append(ingredient)
        with open("ingredients.json", "w") as write_file:
            json.dump(all_ingredients, write_file)

    def __str__(self):
        return f"Pizza of {self.day}: '{self.name}' for - {self.price} grivnas\n" \
               f" ingredients: {self.ingredients}"


class MondayPizza(Pizza):
    """
    Class which creates Monday pizza
    """
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients, "Monday")


class TuesdayPizza(Pizza):
    """
    Class which creates Tuesday pizza
    """
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients, "Tuesday")


class WednesdayPizza(Pizza):
    """
    Class which creates Wednesday pizza
    """
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients, "Wednesday")


class ThursdayPizza(Pizza):
    """
    Class which creates Thursday pizza
    """
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients, "Thursday")


class FridayPizza(Pizza):
    """
    Class which creates Friday pizza
    """
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients, "Friday")


class SaturdayPizza(Pizza):
    """
    Class which creates Saturday pizza
    """
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients, "Saturday")


class SundayPizza(Pizza):
    """
    Class which creates Sunday pizza
    """
    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients, "Sunday")
