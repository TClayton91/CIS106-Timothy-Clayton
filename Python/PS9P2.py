
def battingavg(hits, atbats):
  battingavg = hits / atbats

totalplayers = 0.0
r = input("Do you want to compute batting avg (y/n?")

while r == 'y':
  lastname = input("Enter Last Name")
  hits = float(input("Enter Hits"))
  atbats = float(input("Enter At Bats"))
  battingavg = hits / atbats
  totalplayers = totalplayers + 1
  print("Last Name :",lastname)
  print("Batting Average is:", battingavg)
  r = input("Do you want to compute batting avg (y/n?")

print("Total Number of Players: ", totalplayers)