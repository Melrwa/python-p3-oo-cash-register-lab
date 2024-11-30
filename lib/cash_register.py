#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """
        Initializes the CashRegister with an optional discount and sets the total and items.
        """
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        """
        Adds an item to the register, updates the total, and appends the items list.
        """
        self.total += price * quantity
        self.last_transaction = price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        """
        Applies the discount to the total if applicable, prints success or error message.
        """
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """
        Removes the last added item's value from the total.
        """
        self.total -= self.last_transaction
        self.last_transaction = 0
