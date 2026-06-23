class dmart:
    storename = "DMart"

    def __init__(self, category, product_name, qty, price):
        self.category = category
        self.product_name = product_name
        self.qty = qty
        self.price = price

    @classmethod
    def display_store_details(cls):
        return f"Store Name --> {cls.storename}"

    def common_features(self):
        return f"Category: {self.category}\nProduct Name: {self.product_name}\nQty: {self.qty}\nPrice: {self.price}"


class grocery(dmart):
    def __init__(self, category, product_name, qty, price, brand_name, mfg, exp):
        super().__init__(category, product_name, qty, price)
        self.brand_name = brand_name
        self.mfg = mfg
        self.exp = exp

    def display_grocery_details(self):
        print(super().display_store_details())
        print(super().common_features())
        return f"Brand Name: {self.brand_name}\nMFG: {self.mfg}\nEXP: {self.exp}"


class clothes(dmart):
    def __init__(self, category, product_name, qty, price, colour, size):
        super().__init__(category, product_name, qty, price)
        self.colour = colour
        self.size = size

    def display_clothes_details(self):
        print(super().display_store_details())
        print(super().common_features())
        return f"Colour: {self.colour}\nSize: {self.size}"


c = clothes("clothes", "jeans", 100, 799, "black", "M")
g = grocery("grocery_section", "sugar", 60, 100, "Sugarlite",
            "2026-06-01", "2027-06-01")

while True:
    print("\nWelcome to DMart")
    print("1. Grocery Section")
    print("2. Clothing Section")
    print("3. Purchase Product")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            print(g.display_grocery_details())

        case 2:
            print(c.display_clothes_details())

        case 3:
            print("\n1. Buy Sugar")
            print("2. Buy Jeans")

            p = int(input("Enter product choice: "))

            if p == 1:
                qty = int(input("Enter quantity: "))
                bill = qty * g.price
                print(f"Total Bill = ₹{bill}")

            elif p == 2:
                qty = int(input("Enter quantity: "))
                bill = qty * c.price
                print(f"Total Bill = ₹{bill}")

            else:
                print("Invalid Product Choice!")

        case 4:
            print("Thank You!")
            break

        case _:
            print("Invalid Choice!")
