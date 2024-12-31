import sqlite3
import sys
from credit_card import CreditCard


class BankAccount:

    def __init__(self):

        self.conn = sqlite3.connect("card.s3db")
        self.cur = self.conn.cursor()

        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS card (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    number TEXT NOT NULL UNIQUE,
                    pin TEXT NOT NULL,
                    balance INTEGER DEFAULT 0
                );
                """)

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
                self.conn.close()
                sys.exit()


    def account_menu(self, card_number):
        while True:
            choice = ""
            while choice not in ("1", "2", "0"):
                choice = input("1. Balance\n2. Log out\n0. Exit\n")
            if choice == "1":
                self.cur.execute("SELECT balance FROM card WHERE number = ?", (card_number,))
                balance = self.cur.fetchone()[0]
                print(f"Balance: {balance}")
            elif choice == "2":
                print("\nYou have successfully logged out!\n")
                return
            else:
                print("\nBye!")
                self.conn.close()
                sys.exit()


    def create_account(self):
        card = CreditCard()
        card_number = card.gen_card_number()
        card_pin = card.gen_card_pin()
        self.cur.execute("INSERT INTO card (number, pin) VALUES (?,?)", (card_number, card_pin))
        self.conn.commit()
        print("\nYour card has been created")
        print(f"Your card number:\n{card_number}")
        print(f"Your card pin:\n{card_pin}\n")


    def log_in(self):
        entered_number = input("\nEnter your card number:\n")
        entered_pin = input("Enter your PIN:\n")
        try:
            self.cur.execute("SELECT pin FROM card WHERE number = ?", (entered_number,))
            found_pin = self.cur.fetchone()[0]

            if found_pin == entered_pin:
                print("\nYou have successfully logged in!\n")
                self.account_menu(entered_number)
            else:
                print("Wrong card number or PIN\n")
        except TypeError:
            print("Wrong card number or PIN\n")


BankAccount().main_menu()