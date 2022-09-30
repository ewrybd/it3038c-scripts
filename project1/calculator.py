invalid = "True"

while invalid == 'True':

  operation = input("Select your operation (+,-,*,/): ")

  num1 = int(input("Enter your first number: "))

  num2 = int(input("Enter your second number: "))

  if operation == '+':
    answer = num1 + num2
    print("The number " + str(num1) + " plus " + str(num2) + " equals: " + str(answer))
    break

  elif operation == '-':
    answer = num1 - num2
    print("The number " + str(num1) + " minus " + str(num2) + " equals: " + str(answer))
    break

  elif operation == '*':
    answer = num1 * num2
    print("The number " + str(num1) + " multiplied by " + str(num2) + " equals: " + str(answer))
    break

  elif operation == '/':
    answer = num1 / num2
    print("The number " + str(num1) + " divided by " + str(num2) + " equals: " + str(answer))
    break

  else:
    print("The operation entered: " + operation + " is invalid. Please try again.")