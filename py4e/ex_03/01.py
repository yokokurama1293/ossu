hrs = input("Enter Hours: \n")
rate = input("Enter Rate: \n")

#Convert Hours to float
r = float(rate)
h = float(hrs)

if h > 40 :
    flat = r * 40
    ot   = h - 40
    ot_pay = (ot * 1.5) * ot
    print(flat + ot_pay)

else : 
    print(r * h)