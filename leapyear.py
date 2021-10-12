# find a leap year 
while True:
  userInput = int(input(" Enter a year : "))
  if userInput % 4 == 0:
    print(f"{userInput} is a Leap year.")
  else:
    print(f"{userInput} isn't a Leap year.")
  
  findAgain = input("Find Leap year again (y / n): ")
  if findAgain.lower() != "y":
    break
