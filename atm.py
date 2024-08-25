class AutomatedTMachine:
    def __init__(self, initial_balance=0):  # Corrected __init__ method
        self.balance = initial_balance
        self.pin = '7396'  # Default PIN
        self.transaction_history = []
    def display_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")
    def withdraw_cash(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount:.2f}")
            print(f"Withdrawal successful! You withdrew: ${amount:.2f}")
    def deposit_cash(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount:.2f}")
        print(f"Deposit successful! You deposited: ${amount:.2f}")
    def change_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.pin = new_pin
            print("PIN changed successfully!")
        else:
            print("New PIN must be a 4-digit number.")

    def view_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)
    def run_atm(self):
        while True:
            print("\nWelcome to the ATM!")
            print("T. Check Balance")
            print("H. Withdraw Cash")
            print("A. Deposit Cash")
            print("N. Change PIN")
            print("K. View Transaction History")
            print("S. Exit")

            choice = input("Please choose an option (T-S): ")

            if choice == 'T':
                self.display_currency()
            elif choice == 'H':
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw_currency(amount)
            elif choice == 'A':
                amount = float(input("Enter amount to deposit: "))
                self.deposit_currency(amount)
            elif choice == 'N':
                new_pin = input("Enter new 4-digit PIN: ")
                self.change_pin(new_pin)
            elif choice == 'K':
                self.view_transaction_history()
            elif choice == 'S':
                print("Thank you for using the ATM. Merci!")
                break
            else:
                print("Invalid option! Please choose a valid option.")
if __name__ == "__main__":
    atm = AutomatedTMachine(6000)  
    atm.run_atm()
