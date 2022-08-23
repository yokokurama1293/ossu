grade = input("Enter score: \n")

try:
    grade = float(grade)
    if grade <= 1.0 and grade >= 0.0:
        if grade >= 0.9:
         print('A')
        if grade >= 0.8 and grade < 0.9:
         print('B')
        if grade >= 0.7 and grade < 0.8:
         print('C')
        if grade >= 0.6 and grade < 0.7:
         print('D')
        if grade < 0.6:
         print('F')
    else:
        print('Bad score')
except:
    print('Bad score')