#input phase
nameofappliance = input("Enter Name of Appliance Here")
costofappliance = float(input("Enter Cost of Appliance Here"))

#process phase
if costofappliance>1000:
  Warrenty = costofappliance * 0.10
else:
  Warrenty = costofappliance * 0.05



print(" Name of Appliance: ",nameofappliance)
print(" Cost of Appliance:$",costofappliance)
print("Cost of Warrenty:$",Warrenty)
print("Total with Warrenty:$",costofappliance + Warrenty)