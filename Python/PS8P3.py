# connect to the file
f = open("data1.txt", "r")
total_bonus = 0
c = 0
lastname = f.readline()
#loop as long as the last readline is not null
while lastname != "":
  salary = f.readline()
  print()
  print("Employee Last name:   ", lastname)
  print("Employee Salary is:$  ", format(float(salary), '10,.2f'))
  bonus = float(salary) * 0.10
  print("Employee Bonus:$  ", format(bonus,'10,.2f'))
  total_bonus = total_bonus + bonus
  c = c + 1

f.close()
avg_bonus = total_bonus / c
print("")
print("Average Bonus:$   "), avg_bonus 
format(float((avg_bonus)('10,.2f')))