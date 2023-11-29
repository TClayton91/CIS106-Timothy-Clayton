class student:

  def __init__(self, first, last, districtcode, numcredits):
      self.first = first
      self.last = last
      self.disctrictcode = districtcode
      self.numcredits = numcredits
      self.tuition = tuition

  def fullname(self):
      return '{} {}'.format(self.first, self.last)
    
  

districtcode_input = input("District  Code: ")
numcredits_input = float(input("Number of Credits: "))

if districtcode_input == 'I' :
  tuition = 250.00 * numcredits_input
else:
  tuition = 500.00 * numcredits_input
      

stu_1 = student('Leroy', 'Jenkins', 'districtcode_input', 'numcredits_input')

print("Name:              ",stu_1.fullname())
print("Total Cost:$       ", stu_1.tuition)