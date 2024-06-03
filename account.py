"""Add these methods to the Account class. Add the additional required attributes to the class

Deposit/Withdraw
View Account Details: Method to display the account owner's details and current balance.


Change Account Owner: Method to update the account owner's information.

Account Statement: Method to generate a statement of recent transactions.

Set Overdraft Limit: Method to set an overdraft limit for the account.

Interest Calculation: Method to calculate and apply interest to the balance.

Freeze/Unfreeze Account: Methods to freeze and unfreeze the account for security reasons.

Transaction History: Method to retrieve the history of all transactions made on the account.

Set Minimum Balance: Method to enforce a minimum balance requirement.

Transfer Funds: Method to transfer funds from one account to another.

Close Account: Method to close the account and perform necessary cleanup.

"""
class Account:
    def __init__(self, number, pin, owner_name):
        self.number = number
        self.__pin = pin
        self.__owner_name = owner_name
        self.__balance = 0
        self.__transactions = []

    def deposit(self, amount):
        if amount <= 0:
            return False, "Amount must be positive."
        self.__balance += amount
        self.__transactions.append(f"Deposit: {amount}")
        return True, self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Amount must be positive."
        if amount > self.__balance:
            return False, "Insufficient funds."
        self.__balance -= amount
        self.__transactions.append(f"Withdrawal: {-amount}")
        return True, self.__balance

    def view_account_details(self):
        return f"Account Number: {self.number}\nOwner Name: {self.__owner_name}\nCurrent Balance: {self.__balance}"

    def change_owner(self, new_owner_name):
        if not new_owner_name:
            return False
        self.__owner_name = new_owner_name
        return True

    def generate_statement(self):
        return ''.join(self.__transactions)

    def set_overdraft_limit(self, limit):
        if limit < 0:
            return False
        self.overdraft_limit = limit
        return True

    def calculate_interest(self, rate):
        interest_amount = self.__balance * rate / 100
        self.deposit(interest_amount)
        self.__transactions.append(f"Interest: {interest_amount}")
        return interest_amount

    def freeze_account(self):
        self.frozen = True

    def unfreeze_account(self):
        self.frozen = False

    def is_frozen(self):
        return self.frozen

    def get_transaction_history(self):
        return self.__transactions

    def set_minimum_balance(self, minimum_balance):
        if minimum_balance < 0:
            return False
        self.minimum_balance = minimum_balance
        return True

    def transfer_funds(self, target_account, amount):
        if amount <= 0:
            return False, "Amount must be positive."
        if amount > self.__balance:
            return False, "Insufficient funds."
        success, _ = target_account.deposit(amount)
        if not success:
            return False, "Failed to transfer funds."
        self.withdraw(amount)
        self.__transactions.append(f"Transfer: {amount} to {target_account.number}")
        return True, self.__balance

    def close_account(self):
        return True


if __name__ == "__main__":
    my_account = Account("123456", "1234", "John Doe")

    deposit_success, new_balance = my_account.deposit(500)
    if deposit_success:
        print(my_account.view_account_details())
    else:
        print(deposit_success)

    withdraw_success, new_balance = my_account.withdraw(200)
    if withdraw_success:
        print(my_account.view_account_details())
    else:
        print(withdraw_success)

    my_account.freeze_account()
    print(my_account.is_frozen())

    my_account.unfreeze_account()
    print(my_account.is_frozen()) 

    my_account.transfer_funds(my_account, 100)
    print(my_account.view_account_details())