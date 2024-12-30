import sys
from credit_card import CreditCard


class BankAccount:

    def __init__(self):
        self.cards = {}

    def main_menu(self):
        while True:
            choice = ""
            while choice not in ("1", "2", "0"):
                choice = input("1. Create an account\n2. Log into account\n0. Exit\n")
            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.log_in()
            else:
                print("\nBye!")
                sys.exit()


    def account_menu(self, card_number):
        while True:
            choice = ""
            while choice not in ("1", "2", "0"):
                choice = input("1. Balance\n2. Log out\n0. Exit\n")
            if choice == "1":
                print(f"\nBalance: {self.cards[card_number]["Balance"]}\n")
            elif choice == "2":
                print("\nYou have successfully logged out!\n")
                return
            else:
                print("\nBye!")
                sys.exit()


    def create_account(self):
        card = CreditCard()
        card_number = card.gen_card_number()
        card_pin = card.gen_card_pin()
        self.cards[card_number] = {"Card PIN": card_pin, "Balance": 0}
        print("\nYour card has been created")
        print(f"Your card number:\n{card_number}")
        print(f"Your card pin:\n{card_pin}\n")


    def log_in(self):
        card_number = input("\nEnter your card number:\n")
        card_pin = input("Enter your PIN:\n")
        try:
            if self.cards[card_number]["Card PIN"] == card_pin:
                print("\nYou have successfully logged in!\n")
                self.account_menu(card_number)
            else:
                print("Wrong card number or PIN\n")
        except KeyError:
            print("Wrong card number or PIN\n")


BankAccount().main_menu()