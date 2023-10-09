counter = 0
totalex1 = 0.0

response = input("Do you want to compute your average scores? (Yes or No)") 

while response == "Yes":
  counter = counter + 1
  lastname = input( "Enter Student Last Name")
  Score1 = float(input("Enter Exam Score 1: "))
  Score2 = float(input("Enter Exam Score 2: "))
  average = (Score1 + Score2)/2
  print(lastname, "Has Average of", average)
  totalex1 = totalex1 + Score1
  response = input("Do you want to compute your average scores Yes or No") 

avgex1 = totalex1 / counter
print ("Number of student: ", counter)
print ("Average exam score 1", avgex1)