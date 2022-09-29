import datetime
while True:
    try:
        birthday = input("Please enter your date of birth (Month Day Year):")
        birthday = datetime.datetime.strptime(birthday, '%B %d %Y')
        break
    except:
        print("Format in: (Month Day Year)")

today = datetime.datetime.today()
seconds = (today - birthday).total_seconds()
print("You are: " + str(seconds) + " seconds old!")