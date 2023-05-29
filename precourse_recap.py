
print("Please Add Your Grades Bellow To Get Your Average score :")
maths=input("Maths Grade : ")
english=input("English Grade : ")
pe=input("Physical Education Grade : ")
history=input("History Grade : ")
geog=input("Geography Grade : ")
total_grade=float(maths) + float(english) + float(pe) + float(history) + float(geog)
total_grade=total_grade/5

if total_grade >= 10 :
    print("Congratulations You Passed Your Exams!! With An Average Grade Of : " , total_grade);
else :
    print("Unfortunatly You Didint Pass Your Exams Better Luck Next Time , your Average Grade Is : ", total_grade)