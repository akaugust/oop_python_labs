import json

from pizza import *
from datetime import datetime


class Order:
    """
    Class with Order info(customer, pizza and additional ingredients)
    """
    all_orders = []

    def __init__(self, customer, pizza, *ingredients):
        self.customer = customer
        self.pizza = pizza
        self.ingredients = ingredients
        Order.add_order(self)

    def add_order(self):
        """Adds pizza to the pizzas` file"""
        pizza_info = []
        pizza = {
            "Day": self.pizza.day,
            "Name": self.pizza.name,
            "Price": self.pizza.price,
            "Ingredients": self.pizza.ingredients
        }
        pizza_info.append(pizza)
        order = {
            "Customer": self.customer,
            "Pizza": pizza_info,
            "Ingredients": self.ingredients
        }
        self.all_orders.append(order)
        with open("orders.json", "w") as write_file:
            json.dump(self.all_orders, write_file)

    @property
    def customer(self):
        """Customer getter"""
        return self.__customer

    @customer.setter
    def customer(self, customer):
        """Customer getter"""
        if not isinstance(customer, str):
            raise TypeError("Wrong customer type!")
        if not customer:
            raise ValueError("Wrong value of name!")
        self.__customer = customer

    @property
    def pizza(self):
        """Pizza getter"""
        return self.__pizza

    @pizza.setter
    def pizza(self, pizza):
        """Pizza setter"""
        if not isinstance(pizza, Pizza):
            raise TypeError("That is not a Pizza type!")
        self.__pizza = pizza

    @property
    def ingredients(self):
        """Ingredients getter"""
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        """Ingredients setter"""
        if any(not isinstance(ingredient, str) for ingredient in ingredients):
            raise TypeError("Wrong type of ingredients")
        with open("ingredients.json", "r") as read_file:
            ingredients_data = json.load(read_file)
        for ingredient in ingredients:
            if ingredient not in ingredients_data:
                raise ValueError("This ingredient cannot ne added!")
            self.add_ingredient(ingredient)
        self.__ingredients = list(ingredients)

    def add_ingredient(self, ingredient):
        """Function that adds ingredients to the order"""
        if ingredient in self.pizza.ingredients:
            raise ValueError("You can`t add the ingredient that is already in pizza!")
        self.pizza.ingredients.append(ingredient)

    def del_ingredient(self, ingredient):
        """Function that deletes ingredients from the order"""
        if ingredient not in self.pizza.ingredients:
            raise ValueError("This ingredient is not in pizza!")
        self.pizza.ingredients.remove(ingredient)

    @staticmethod
    def get_pizza_of_the_day():
        day = datetime.now().strftime("%A")
        with open("pizzas_of_the_day.json", "r") as read_file:
            pizza_data = json.load(read_file)
        for p_o_d in pizza_data:
            if p_o_d.get("Day") == day:
                return p_o_d

    def __str__(self):
        return f"\nOrder from Customer '{self.__customer}':\n" \
               f"{self.__pizza}"


if __name__ == '__main__':
    Pizza.add_all_ingredients("tomatoes", "mozzarella cheese", "basil", "pepperoni", "parmesan cheese", "feta cheese", "pineapple", "chicken",
                        "corn", "mushrooms", "bacon", "onion", "sauce" "pepper", "salt", "sugar", "parsley")
    monday_pizza = MondayPizza("Margarita", 250, ["tomatoes", "mozzarella cheese", "basil"])
    tuesday_pizza = TuesdayPizza("Pepperoni", 225, ["pepperoni", "mozzarella cheese", "tomatoes"])
    wednesday_pizza = WednesdayPizza("FourCheese", 175, ["mozzarella cheese", "parmesan cheese", "feta cheese"])
    thursday_pizza = ThursdayPizza("Hawaii", 275, ["pineapple", "chicken", "corn"])
    friday_pizza = FridayPizza("White", 250, ["mushrooms", "mozzarella cheese", "chicken"])
    saturday_pizza = SaturdayPizza("Vegetarian", 250, ["tomatoes", "mushrooms", "basil"])
    sunday_pizza = SundayPizza("Barbeque", 375, ["chicken", "bacon", "onion"])

    print(monday_pizza, tuesday_pizza, wednesday_pizza, thursday_pizza, friday_pizza, saturday_pizza, sunday_pizza, sep='\n')

    order1 = Order("A", thursday_pizza, "basil", "bacon")
    print(order1)
    order1.del_ingredient("chicken")
    print(order1)

    print(Order.get_pizza_of_the_day())
