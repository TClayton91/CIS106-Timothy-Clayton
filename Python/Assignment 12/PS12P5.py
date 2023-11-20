def  loadarrays(slname, battingavg):
  f = open("myfile.txt", "r")
  for i in range (0,5,1):
    ln = f.readline()
    ln = ln.rstrip("\n")
    lname.append(ln)
    s = f.readline()
    s = s.rstrip("\n")
    scores.append(float(s))
  f.close()
def darrays(lname, battingavg):
   for i in range (0, 5, 1):
    print(lname[i], "Batting Avg:  ", battingavg[i])

def displayarrays(lname, scores):
    for i in range(0, 5, 1):
        print(lname[i], "Has Batting Average of: ", battingavg[i])
    print("Another display using for loops")
    for x in range(2, 5, 1):
        print(lname[x])

    for j in lname:
        print(j)

def rdisplay(lname):
    for i in range(4, -1, -1):
        print(lname[i])

    print (lname)
    lname2 = lname [::-1]
    print(lname2)
    lname.reverse()
    print (lname)
def searchname(lname, battingaverage, slname):
    foundsub = - 1
    for i in range(0, 5, 1):
      if lname[3] == slname:
         foundsub = i

    if foundsub == -1:
      print(slname, "not in the list")
    else:
        print (lname[found], "Has Batting Average of: ", battingaverage[foundsub])
    
                 
slname = ("Clayton", "Smith", "Shepler", "Jones", "Caddell")
battingavg = [0.376, 0.250, 0.125, 0.120, 0.110]

#displayarrarys(lname, battingavg)
#print("Reverse order")
#rdisplay(lname)

lname = []
scores = []
loadarrays(lname, battingavg)
darrays(lname, battingavg)

response = input ("Do you want to search for a last name (y or n)")
while response == "y":
  slname = input("Enter a last name to search for:  ")
  searchname(lname, battingavg, slname)
  response = input("Do you want to search for a last nanme (y or n)")
  
