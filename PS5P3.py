#input phase
numberofbooks = float(input("Enter Number Of Books Here"))
costperbook = float(input("Enter Cost Per Book Here"))

#process phase
ordertotal = numberofbooks * costperbook
if numberofbooks>50:
  Shipping = 0
else:
  Shipping = 25.00



print(" Order Total:$ ",ordertotal)
print(" Shipping Cost:$",Shipping)