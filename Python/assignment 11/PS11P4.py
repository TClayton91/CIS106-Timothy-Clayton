def BowlAverage (score1,score2,score3,handi):
  sum = score1 + score2 + score3
  average = (sum / 3)
  haverage = (sum + handi) / 3
  return average,haverage

lastname = input("Enter Last Name:       ")
score1 = float(input("Enter Score 1:     "))
score2 = float(input("Enter Score 2:     "))
score3 = float(input("Enter Score 3:     "))
handi = float(input("What is your Handicap:"))
average,haverage = BowlAverage(score1,score2,score3,handi)
print("Bowler Name:   ",lastname)
print("Average Score: ",average)
print("Handicap:      ",haverage)