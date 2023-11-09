def salesreport (sales):
  if sales > 100000:
    commission = sales * 0.10
  elif sales <= 100000:
    commission = sales * 0.05
  nextyearssalegoal = sales * 1.05
  return commission,nextyearssalegoal

salesperson = input("Enter Salesperson lastname: ")
sales = float(input("Enter Sales: "))
commission,nextyearssalegoal = salesreport(sales)
print("Salesperson Name: ",salesperson)
print("Commission: ",commission)  
print("Next Years Target Sales",nextyearssalegoal)
