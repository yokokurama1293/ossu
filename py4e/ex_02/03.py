hours = input("How many hours did you work this week? \n")
rate = input("What is your hourly rate? \n")
#Convert string to int and int to float
hours = int(hours)
rate = int(rate)
total = float(rate * hours)

#All Done
print("You made $", total, "this pay period")