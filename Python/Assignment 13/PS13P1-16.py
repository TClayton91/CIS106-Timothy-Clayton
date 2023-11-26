def dl1 (mylist):
  n = int(input("Number of items or you list"))
  for n in range(0,n,1):
    s = int(input("Enter an integer"))
    mylist.append(s)
  return mylist
def displaylist(mylist):
  for item in mylist:
      print(item)

#main
mylist = []   # defining an empty list
mylist = dl1(mylist)
displaylist(mylist)
print(mylist)

#dl2
mylist.insert(0,99)
print(mylist)
#dl3
mylist[0] = 100
print(mylist)
#dl4
mylist2 = [500,600,700,800,900]
mylist2.extend(mylist)
print(mylist2)
#dl5
mylist2.remove(800)
print(mylist2)
#dl6
mylist.remove(100)
print(mylist2)
#dl7
mylist3 = ["A", "B", "C", "A", "A", "C"]
print("Number of A in mygrades is ", mylist3.count("A"))
#dl9
print ("B Position in the list", mylist3.index("B"))
#dl10
print ("Number of F in mygrades is " , mylist3.count("F"))
if "F" == 0:
  print ("No F in mygrades")
#dl11
mylist2.clear()
print(mylist2)
#dl12
del mylist2
print(mylist2)
#dl13
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
#Dl14
sorted(players)
print(players)

#dl15
backward_players2 = players.copy()
print("Players 2:  ", backward_players2)
backward_players2.reverse()
print("Players 2 reversed:  ", backward_players2)
