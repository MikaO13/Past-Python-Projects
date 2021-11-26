class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
    
  def __repr(self):
    return "%s's account. Balance: $%.2f" % (self.name, self.balance)
  
  def show_balance(self):
    print "%s's account. Balance: $%.2f" % (self.name, self.balance)
    
  def deposit(self, amount):
    if amount <= 0:
      print "Error! Invalid amount entered."
      return
    else:
      print "Deposit Amount: " + str(amount)
      self.balance += amount
      self.show_balance()
  
  def withdraw(self, amount):
    if amount <= 0 or amount > self.balance:
      print "Error! Invalid amount entered."
      return
    else:
      print "Withdrawal Amount: " + str(amount)
      self.balance -= amount
      self.show_balance()

my_account = BankAccount("Mika")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account