def displayarrays(lname, Examscores):

  for i in range (0, 1, 1):
    print(lname[i], "Exam Score:", Examscores[i])

   
  for x in range(1, 10, 1):
     print(lname[x])

def rdisplay(lname):
   for i in range (9, -1, -1):
      print(lname[i])


  
lname = ["Clayton", "Jones", "Baker", "Shepler", "Culver", "Caddell", "Brady", "Smith", "Schmidt", "Bates"]

def displayarrays(lname, Examscores):
    for i in range(len(lname)):
        print(lname[i], "Exam Score:", Examscores[i])
Examscores = [80.0, 50.0, 66.0, 78.0, 86.0, 76.0, 90.0, 55.0, 66.0, 77.0]

displayarrays(lname, Examscores)

