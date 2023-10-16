f = open("data1.txt", "r")

c = 0
totaltuition = 0.0

#get first part of the data

lastname = f.readline()

while lastname != "": # detect end of file
  dcode = f.readline()
  credits = float(f.readline())

 if decode == 'I':
     costpercredit = 250.00
 else:
    costpercredit = 500.00

  tuition = credits * costpercredit
  totaltuition = totaltuition + tuition
  c = c + 1

  print ("Student:  ", lastname)
  print ("Credits Taken:  ", credits)
  print ("Tuition Owed", tuition)

  lastname = f.readline()

f.close()

print("Number of Students", c)
print("Total Tuition Owed", totaltuition)