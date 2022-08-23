hours = input("Enter Hours: \n")
rate = input("Enter Rate: \n")

try:
    hours = float(hours)
    rate  = float(rate)
    if hours > 40 :
        flat = rate * 40
        ot   = hours - 40
        ot_pay = ot * 1.75
        print(flat + ot_pay)
    else : 
        print(rate * hours)
except:
    print('Error, please enter numeric input')