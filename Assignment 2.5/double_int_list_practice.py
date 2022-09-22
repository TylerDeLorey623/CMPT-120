def main():
  #set this to any double
  doubleValue = 3.14
  
  #set this to any int
  intValue = 10
  
  #print out addition, subtraction, multiplication, and division of these two values

  print("Addition:", intValue + doubleValue)
  print("Subtraction:", intValue - doubleValue)
  print("Multiplication:", intValue * doubleValue)
  print("Division:", intValue / doubleValue)
  
  #populate this list
  myFriends = ["Chris", "Kristen", "Lauren", "Daniel", "Ian"]
  
  #print out your friends at index 2 and index 3
  print(myFriends[2])
  print(myFriends[3])
  
  #populate this list with five numbers
  fiveNumbers = [10, 20, 30, 40, 50]
  
  #do each of the four equations with different numbers each time.
  print("Addition:", fiveNumbers[2] + fiveNumbers[4])
  print("Subtraction:", fiveNumbers[1] - fiveNumbers[0])
  print("Multiplication:", fiveNumbers[0] * fiveNumbers[3])
  print("Division:", fiveNumbers[3] / fiveNumbers[1])
  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)
  fiveNumbers[3] = 60
  fiveNumbers[4] = 100

  #print out the list
  print(fiveNumbers)


main()
