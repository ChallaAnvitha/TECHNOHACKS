class ATM:
  def __init__(self, balance=0):
    self.balance = balance

  def check_balance(self):
    return f"Your balance is ${self.balance}"

  def deposit(self, amount):
    self.balance += amount
    return f"${amount} deposited successfully. Your new balance is ${self.balance}"

  def withdraw(self, amount):
   if self.balance >= amount:
    self.balance -= amount
    return f"${amount} withdrawn successfully. Your new balance is ${self.balance}"
   else:
     return "Insufficient funds. Please try again."

def main():
 atm = ATM()
 while True:
  print("Choose an option:")
  print("1. Check Balance")
  print("2. Deposit")
  print("3. Withdraw")
  print("4. Quit")
  choice = input("Enter your choice (1/2/3/4): ")

  if choice == '1':
    print(atm.check_balance())
  elif choice == '2':
    amount = float(input("Enter amount to deposit: "))
    print(atm.deposit(amount))
  elif choice == '3':
    amount = float(input("Enter amount to withdraw: "))
    print(atm.withdraw(amount))
  elif choice == '4':
    print("Exiting the program.")
    break
  else:
    print("Invalid choice. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
  main()
