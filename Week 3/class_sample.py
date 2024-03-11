marks = 80
result =''
if marks <30:
  result="Failed"
elif marks >75:
  result="Passed with distinction"
else:
  result="Passed"

print(result)

def checkVowel(n):
  match n:
    case 'a': return "Vowel alphabet"
    case 'e': return "Vowel alphabet"
    case 'i': return "Vowel alphabet"
    case 'o': return "Vowel alphabet"
    case 'u': return "Vowel alphabet"
    case _: return "Simple alphabet"
print (checkVowel('a'))
print (checkVowel('m'))
print (checkVowel('y'))
"""
class Python_Switch:
  def day(self, month):
    default = "Incorrect Day"
    return getattr(self, 'case_' + str(month), lambda: default)()
  def case_1(self):
    return "Jan"
  def case_2(self):
    return "Feb"
  def case_3(self):
    return "Mar"
switch=Python_Switch
print(switch.day(1))
print(switch.day(2))
print(switch.day(3)) """

words=["one", "two", "three"]
for x in words:
  print(x)