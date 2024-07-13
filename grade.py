grade = int(input("What grade did I get? Enter a grade number: "))
if grade >= 90:
  print("You got an A!")
elif grade <= 89 and grade >= 80:
  print("You got a B")
elif grade <= 79 and grade >= 70:
  print("You got a C")
elif grade <= 69 and grade >= 60:
  print("You got a D")
elif grade <= 59 and grade >= 0:
  print("You got an F")
else:
  print("Type in grade number to see your grade letter. ")