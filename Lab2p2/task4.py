class Product:
    """
    Class with product`s info(name, price, code)
    """
    all_codes = []

    def __init__(self, name, price, code):
        self.name = name
        self.price = price
        self.code = code

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Wrong type of name!")
        if not name or name.__contains__(" "):
            raise ValueError("Wrong product of name!")
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, int):
            raise TypeError("Wrong type of price!")
        if price <= 0:
            raise ValueError("Price can`t be 0 or lower!")
        self.__price = price

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        if not isinstance(code, int):
            raise TypeError("Wrong type of code!")
        if code <= 0:
            raise ValueError("Сode can`t be negative or zero!")
        if code in self.all_codes:
            raise ValueError("This record book number already exists!")
        self.all_codes.append(code)
        self.__code = code

    def __str__(self):
        return f"Product {self.__name} - {self.__price} grivnas, code: {self.__code}"


class Node:
    """
    Class with Binary Search Tree
    """
    all_tree_products = []

    def __init__(self, product):
        self.left = None
        self.right = None
        self.product = product

    def insert(self, product):
        if not isinstance(product, Product):
            raise TypeError("Wrong type of insert!")
        if self.product:
            if product.code < self.product.code:
                if self.left is None:
                    if product.code not in self.all_tree_products:
                        self.left = Node(product)
                        self.all_tree_products.append(product.code)
                    else:
                        raise ValueError("You can`t add same products!")
                else:
                    self.left.insert(product)
            elif product.code > self.product.code:
                if self.right is None:
                    if product.code not in self.all_tree_products:
                        self.right = Node(product)
                        self.all_tree_products.append(product.code)
                    else:
                        raise ValueError("You can`t add same products!")
                else:
                    self.right.insert(product)
            elif product not in self.all_tree_products:
                self.all_tree_products.append(product)
                self.product = product
            else:
                raise ValueError("You can`t add same products!")

    def find_value(self, code):
        if code < self.product.code:
            if self.left is None:
                raise ValueError("There is no product with such code!")
            return self.left.find_value(code)
        elif code > self.product.code:
            if self.right is None:
                raise ValueError("There is no product with such code!")
            return self.right.find_value(code)
        else:
            return self.product.price

    def find_cost(self, code, number):
        if self.find_value(code):
            return f"Cost of [{code}] with number of {number} is {self.find_value(code) * number}"

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(f"Product code: {self.product}")
        if self.right:
            self.right.print_tree()


if __name__ == '__main__':

    tea = Product("Tea", 25, 1)
    water = Product("Water", 14, 5)
    crisps = Product("Crisps", 15, 3)
    coffee = Product("Coffee", 56, 4)

    root = Node(tea)
    root.insert(water)
    root.insert(crisps)
    root.insert(coffee)
    root.print_tree()

    print(root.find_cost(3, 2))
