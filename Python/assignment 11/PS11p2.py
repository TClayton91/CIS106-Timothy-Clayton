def examaverage (exam1,exam2,exam3):
  sum = exam1 + exam2 + exam3
  total = 300
  percentage = (sum/total) * 100
  examavg = sum / 3
  return examavg,sum

lastname = input("Enter Last Name: ")
exam1 = float(input("Enter Exam 1 Score: "))
exam2 = float(input("Enter Exam 2 Score: "))
exam3 = float(input("Enter Exam 3 Score: "))

examaverage,sum = examaverage(exam1,exam2,exam3)
print("Last Name: ",lastname)
print("Average Exam Score: ",examaverage)
print("Total Exam Points: ",sum)