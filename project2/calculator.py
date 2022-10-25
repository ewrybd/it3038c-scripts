invalid = "True"

while invalid == 'True':

  operation = input("Select your operation out of the following: (Addition: +, Subtraction: -, Multiplication: *, Division: /, Exponentiation: ^, Modulus: %, or # to enter from 3 to 6 numbers at once.) ")

  if operation == '+':
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    answer = num1 + num2
    print("The number " + str(num1) + " plus " + str(num2) + " equals: " + str(answer))
    break

  elif operation == '-':
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    answer = num1 - num2
    print("The number " + str(num1) + " minus " + str(num2) + " equals: " + str(answer))
    break

  elif operation == '*':
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    answer = num1 * num2
    print("The number " + str(num1) + " multiplied by " + str(num2) + " equals: " + str(answer))
    break

  elif operation == '/':
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    answer = num1 / num2
    print("The number " + str(num1) + " divided by " + str(num2) + " equals: " + str(answer))
    break

  elif operation == '^':
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    answer = num1 ** num2
    print("The number " + str(num1) + " to the power of " + str(num2) + " equals: " + str(answer))
    break

  elif operation == '%':
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    answer = num1 % num2
    print("The number " + str(num1) + " modulus of " + str(num2) + " equals: " + str(answer))
    break

  elif operation == '#':
    operation2 = input("What operation would you like to complete? (+, -, *, /) ")
    
    if operation2 == '+':
      numbers = int(input("How many numbers would you like to input? (3-6) "))
      if numbers == 3:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = int(input("Enter your third number: "))
        answer = num1 + num2 + num3
        print("The numbers: " + str(num1) + ", " + str(num2) + ", and " + str(num3) + " added together equal: " + str(answer))
        break

      elif numbers == 4:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = int(input("Enter your third number: "))
        num4 = int(input("Enter your fourth number: "))
        answer = num1 + num2 + num3 + num4
        print("The numbers: " + str(num1) + ", " + str(num2) + ", " + str(num3) + ", and " + str(num4) + " added together equal: " + str(answer))
        break

      elif numbers == 5:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = int(input("Enter your third number: "))
        num4 = int(input("Enter your fourth number: "))
        num5 = int(input("Enter your fifth number: "))
        answer = num1 + num2 + num3 + num4 + num5
        print("The numbers: " + str(num1) + ", " + str(num2) + ", " + str(num3) + ", " + str(num4) + ", and " + str(num5) + " added together equal: " + str(answer))
        break

      elif numbers == 6:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = int(input("Enter your third number: "))
        num4 = int(input("Enter your fourth number: "))
        num5 = int(input("Enter your fifth number: "))
        num6 = int(input("Enter your sixth number: "))
        answer = num1 + num2 + num3 + num4 + num5 + num6
        print("The numbers: " + str(num1) + ", " + str(num2) + ", " + str(num3) + ", " + str(num4) + ", " + str(num5) + ", and " + str(num6) + " added together equal: " + str(answer))
        break

      else:
        print("The amount of numbers entered: " + str(numbers) + " is invalid. Please try again.")

    elif operation2 == '-':
      numbers = int(input("How many numbers would you like to input? (3-6) "))
      if numbers == 3:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = int(input("Enter your third number: "))
        answer = num1 - num2 - num3
        print("The number " + str(num1) + " subtracted by " + str(num2) + ", and then by " + str(num3) + ", equals: " + str(answer))
        break

      elif numbers == 4:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = int(input("Enter your third number: "))
        num4 = int(input("Enter your fourth number: "))
        answer = num1 - num2 - num3 - num4
        print("The number " + str(num1) + " subtracted by the following: " + str(num2) + ", " + str(num3) + ", and " + str(num4) + " equals: " + str(answer))
        break

      elif numbers == 5:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = int(input("Enter your third number: "))
        num4 = int(input("Enter your fourth number: "))
        num5 = int(input("Enter your fifth number: "))
        answer = num1 - num2 - num3 - num4 - num5
        print("The number " + str(num1) + " subtracted by the following: " + str(num2) + ", " + str(num3) + ", " + str(num4) + ", and " + str(num5) + " equals: " + str(answer))
        break

      elif numbers == 6:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = int(input("Enter your third number: "))
        num4 = int(input("Enter your fourth number: "))
        num5 = int(input("Enter your fifth number: "))
        num6 = int(input("Enter your sixth number: "))
        answer = num1 - num2 - num3 - num4 - num5 - num6
        print("The number " + str(num1) + " subtracted by the following: " + str(num2) + ", " + str(num3) + ", " + str(num4) + ", " + str(num5) + ", and " + str(num6) + " equals: " + str(answer))
        break

      else:
        print("The amount of numbers entered: " + str(numbers) + " is invalid. Please try again.")

    elif operation2 == '*':
      numbers = int(input("How many numbers would you like to input? (3-6) "))
      if numbers == 3:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = int(input("Enter your third number: "))
        answer = num1 * num2 * num3
        print("The numbers: " + str(num1) + ", " + str(num2) + ", and " + str(num3) + " multiplied together equal: " + str(answer))
        break

      elif numbers == 4:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = int(input("Enter your third number: "))
        num4 = int(input("Enter your fourth number: "))
        answer = num1 * num2 * num3 * num4
        print("The numbers: " + str(num1) + ", " + str(num2) + ", " + str(num3) + ", and " + str(num4) + " multiplied together equal: " + str(answer))
        break

      elif numbers == 5:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = int(input("Enter your third number: "))
        num4 = int(input("Enter your fourth number: "))
        num5 = int(input("Enter your fifth number: "))
        answer = num1 * num2 * num3 * num4 * num5
        print("The numbers: " + str(num1) + ", " + str(num2) + ", " + str(num3) + ", " + str(num4) + ", and " + str(num5) + " multiplied together equal: " + str(answer))
        break

      elif numbers == 6:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = int(input("Enter your third number: "))
        num4 = int(input("Enter your fourth number: "))
        num5 = int(input("Enter your fifth number: "))
        num6 = int(input("Enter your sixth number: "))
        answer = num1 * num2 * num3 * num4 * num5 * num6
        print("The numbers: " + str(num1) + ", " + str(num2) + ", " + str(num3) + ", " + str(num4) + ", " + str(num5) + ", and " + str(num6) + " multiplied together equal: " + str(answer))
        break

      else:
        print("The amount of numbers entered: " + str(numbers) + " is invalid. Please try again.")

    elif operation2 == '/':
      numbers = int(input("How many numbers would you like to input? (3-6) "))
      if numbers == 3:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = int(input("Enter your third number: "))
        answer = num1 / num2 / num3
        print("The number " + str(num1) + " divided by " + str(num2) + ", and then by " + str(num3) + ", equals: " + str(answer))
        break

      elif numbers == 4:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = int(input("Enter your third number: "))
        num4 = int(input("Enter your fourth number: "))
        answer = num1 / num2 / num3 / num4
        print("The number " + str(num1) + " divided by the following: " + str(num2) + ", " + str(num3) + ", and " + str(num4) + " equals: " + str(answer))
        break

      elif numbers == 5:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = int(input("Enter your third number: "))
        num4 = int(input("Enter your fourth number: "))
        num5 = int(input("Enter your fifth number: "))
        answer = num1 / num2 / num3 / num4 / num5
        print("The number " + str(num1) + " divided by the following: " + str(num2) + ", " + str(num3) + ", " + str(num4) + ", and " + str(num5) + " equals: " + str(answer))
        break

      elif numbers == 6:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        num3 = int(input("Enter your third number: "))
        num4 = int(input("Enter your fourth number: "))
        num5 = int(input("Enter your fifth number: "))
        num6 = int(input("Enter your sixth number: "))
        answer = num1 / num2 / num3 / num4 / num5 / num6
        print("The number " + str(num1) + " divided by the following: " + str(num2) + ", " + str(num3) + ", " + str(num4) + ", " + str(num5) + ", and " + str(num6) + " equals: " + str(answer))
        break

      else:
        print("The amount of numbers entered: " + str(numbers) + " is invalid. Please try again.")

    else:
      print("The operation entered: " + operation2 + " is invalid. Please try again.")

  else:
    print("The operation entered: " + operation + " is invalid. Please try again.")