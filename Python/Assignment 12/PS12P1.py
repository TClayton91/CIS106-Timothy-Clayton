def displayarrays(lname):

  for i in range (0, 1, 1):
    print(lname[i])

   
  for x in range(1, 10, 1):
     print(lname[x])



def rdisplay(lname):
   for i in range (9, -1, -1):
      print(lname[i])

  


  
lname = ["Clayton", "Jones", "Baker", "Shepler", "Culver", "Caddell", "Brady", "Smith", "Schmidt", "Bates"]

displayarrays(lname)
print("reverse order")
rdisplay(lname)
