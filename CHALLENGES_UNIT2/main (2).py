class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__initial_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__initial_balance += amount
      print("Deposited RS {}. New Balance RS {}".format(
          amount, self.__initial_balance))
    else:
      print("Invalid Deposit Amount\n Please Deposit A Amount")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__initial_balance:
      self.__initial_balance -= amount
      print("Withdrew RS {}. New Balance RS {}".format(amount,
                                                       self.__initial_balance))
    else:
      print("Invalid withdraw amount or insufficient balance")

  def display_balance(self):
    print("Account Balance For {} (Acount Number #{}) RS{} ".format(
        self.__account_number, self.__account_holder_name,
        self.__initial_balance))


account = BankAccount(account_number="4857979482",
                      account_holder_name="Harish",
                      initial_balance=10000.0)

account.display_balance()
account.deposit(5000.0)
account.withdraw(1500.0)
account.display_balance()
