#This starts the loop to bullet proof invalid input
invalid = "True"

while invalid == 'True':

  operation = input("Select your operation out of the following: (Addition: +, Subtraction: -, Multiplication: *, Division: /, Exponentiation: ^, Modulus: %, Floor Division: //) ")

#This distinguishes the operation that was entered by the user

  if operation == '+': #Addition Loop to allow user to enter as many numbers as they want
      done = 'False'
      answer = int(0)
      while done == 'False':
        num = int(input("Enter a number to add: "))
        answer += num
        print("The total sum so far is: " + str(answer))
        proceed = input("Would you like to continue? [Y/N] ")
        if proceed == 'Y':
          done = 'False'
        else:
          done = 'True'
          break
      break

  elif operation == '-': #Subtraction Loop to allow user to enter as many numbers as they want
      done = 'False'
      answer = int(input("Enter your first number that will be subtracted from: "))
      while done == 'False':
        num = int(input("Enter a number to subtract: "))
        answer -= num
        print("The total difference so far is: " + str(answer))
        proceed = input("Would you like to continue? [Y/N] ")
        if proceed == 'Y':
          done = 'False'
        else:
          done = 'True'
          break
      break

  elif operation == '*': #Multiplication Loop to allow user to enter as many numbers as they want
      done = 'False'
      answer = int(1)
      while done == 'False':
        num = int(input("Enter a number to multiply: "))
        answer *= num
        print("The total product so far is: " + str(answer))
        proceed = input("Would you like to continue? [Y/N] ")
        if proceed == 'Y':
          done = 'False'
        else:
          done = 'True'
          break
      break

  elif operation == '/': #Division Loop to allow user to enter as many numbers as they want
      done = 'False'
      answer = int(input("Enter your first number that will be divided from: "))
      while done == 'False':
        num = int(input("Enter a number to divide: "))
        answer /= num
        print("The total quotient so far is: " + str(answer))
        proceed = input("Would you like to continue? [Y/N] ")
        if proceed == 'Y':
          done = 'False'
        else:
          done = 'True'
          break
      break

  elif operation == '^': #Exponentiation Loop to allow user to enter as many numbers as they want
      done = 'False'
      answer = int(input("Enter your first number that will use exponentiation: "))
      while done == 'False':
        num = int(input("Enter a number to be the power: "))
        answer **= num
        print("The total exponentiation so far is: " + str(answer))
        proceed = input("Would you like to continue? [Y/N] ")
        if proceed == 'Y':
          done = 'False'
        else:
          done = 'True'
          break
      break

  elif operation == '%': #Modulus Loop to allow user to enter as many numbers as they want
      done = 'False'
      answer = int(input("Enter your first number that will use modulus: "))
      while done == 'False':
        num = int(input("Enter a number to find the remainder: "))
        answer %= num
        print("The total result so far is: " + str(answer))
        proceed = input("Would you like to continue? [Y/N] ")
        if proceed == 'Y':
          done = 'False'
        else:
          done = 'True'
          break
      break

  elif operation == '//': # Floor Division Loop to allow user to enter as many numbers as they want
      done = 'False'
      answer = int(input("Enter your first number that will use floor division: "))
      while done == 'False':
        num = int(input("Enter a number to floor divide: "))
        answer //= num
        print("The total quotient so far is: " + str(answer))
        proceed = input("Would you like to continue? [Y/N] ")
        if proceed == 'Y':
          done = 'False'
        else:
          done = 'True'
          break
      break

  else:
    print("The operation entered: " + operation + " is invalid. Please try again.") #Notifies user of invalid input and loops to make them enter a valid operation