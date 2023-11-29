class employee:

  def __init__(self, first, last, pay, bonusrate):
      self.first = first
      self.last = last
      self.pay = pay
      self.bonusrate = bonusrate
      self.bonus = (bonusrate * pay)
      self.email = first + '.' + last + '@company.com'

  def fullname(self):
      return '{} {}'.format(self.first, self.last)
    
  def apply_bonus(self):
     self.pay = int(self.pay * self.bonusrate / 100)

bonusrate_input = float(input("Enter Bonus Rate: "))
      

emp_1 = employee('Leroy', 'Jenkins', 50000, bonusrate_input)

print(emp_1.fullname())
print(emp_1.pay)
print(emp_1.email)
print(emp_1.bonus)