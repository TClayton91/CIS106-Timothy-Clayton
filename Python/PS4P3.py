#input phase
from typing_extensions import TypeAliasType


totalformeal = float(input("Enter price of meal"))

#process phase
fifteentip =totalformeal * 0.15
eightteentip = totalformeal * 0.18
twentytip = totalformeal * 0.20

#outputphase
print("With 15% tip")
print("Total",totalformeal)
print("Tip",fifteentip)
print("Total with Tip",totalformeal+fifteentip)

print("With 18% tip")
print("Total",totalformeal)
print("Tip",eightteentip)
print("Total with Tip",totalformeal+eightteentip)

print("With 20% tip")
print("Total",totalformeal)
print("Tip",twentytip)
print("Total with Tip",totalformeal+twentytip)