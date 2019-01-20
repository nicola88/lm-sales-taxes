import math

from decimal import Decimal
from enum import Enum
from functools import reduce
from typing import List


class ProductCategory(Enum):
    OTHER = 0
    FOOD = 1
    BOOK = 2
    MEDICAL = 3


class Product:

    def __init__(self, name: str, price: Decimal, category: ProductCategory, imported: bool = False):
        if name:
            self.name = name
        else:
            raise ValueError("The product name must be a non-empty string")
        if price >= Decimal(0):
            self.price = price
        else:
            raise ValueError("The product price must be equal or greater than zero")
        if category:
            self.category = category
        else:
            raise ValueError("The product category must be provided")
        self.imported = imported

    def __str__(self):
        return self.name

    def get_taxes(self):
        sales_taxes = Decimal(0)
        if self.category is ProductCategory.OTHER:
            sales_taxes += self.price * Decimal('0.1')
        if self.imported:
            sales_taxes += self.price * Decimal('0.05')
        return App.round_decimal(sales_taxes)

    # def get_price_after_taxes(self):
    #     return self.price + self.get_taxes()


class ProductPurchase:

    def __init__(self, product: Product, quantity: int):
        if product:
            self.product = product
        else:
            raise ValueError("The product must be a non-empty value")
        if quantity >= 1:
            self.quantity = quantity
        else:
            raise ValueError("The product quantity must be grater than zero")

    def get_price(self) -> Decimal:
        return (self.product.price + self.product.get_taxes()) * self.quantity

    def get_taxes(self) -> Decimal:
        return self.product.get_taxes() * self.quantity


class Receipt:

    def __init__(self):
        self.purchases: List[ProductPurchase] = []

    def add_purchase(self, purchase: ProductPurchase):
        if purchase:
            self.purchases.append(purchase)

    def get_total(self) -> Decimal:
        return reduce(lambda c1, c2: c1 + c2, map(lambda p: p.get_price(), self.purchases))

    def get_sales_taxes(self) -> Decimal:
        return reduce(lambda t1, t2: t1 + t2, map(lambda p: p.get_taxes(), self.purchases))

    def show(self):
        for purchase in self.purchases:
            print("{} {}: {}".format(
                purchase.quantity, purchase.product, round(purchase.get_price(), 2))
            )
        print()
        print("Sales Taxes: {}".format(round(self.get_sales_taxes(), 2)))
        print()
        print("Total: {}".format(round(self.get_total(), 2)))


class App:

    @staticmethod
    def run_simulation(purchase_file: str) -> Receipt:
        import os
        if not os.path.exists(purchase_file):
            raise ValueError("Purchase file not found at", purchase_file)
        with open(purchase_file, 'r') as purchase_file:
            import csv
            from distutils.util import strtobool
            receipt = Receipt()
            reader = csv.reader(purchase_file)
            next(reader)  # Skip CSV headers
            for row in reader:
                name = row[0]
                price = Decimal(row[1])
                category = ProductCategory[row[2].upper()]
                imported = bool(strtobool(row[3]))
                quantity = int(row[4])
                purchase = ProductPurchase(Product(name, price, category, imported), quantity)
                receipt.add_purchase(purchase)
            return receipt

    @staticmethod
    def round_decimal(amount: Decimal, precision: int = 2, unit: Decimal = Decimal('0.05')) -> Decimal:
        if not amount:
            return amount
        if precision < 0:
            raise ValueError("Rounding precision must be greater or equal than zero")
        if unit <= Decimal(0):
            raise ValueError("Rounding unit must be greater than zero")
        rounded_decimal = round(amount, precision)
        rc = rounded_decimal / unit
        is_rounded = math.modf(rc)[0] == Decimal(0)
        increment = Decimal(0)
        while not is_rounded:
            increment += Decimal(1) / (10 ** precision)
            rc = (rounded_decimal + increment) / unit
            is_rounded = math.modf(rc)[0] == Decimal(0)
        return rounded_decimal + increment
