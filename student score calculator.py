student_score=input("enter your student_score")
student_score=float(student_score)
student_score=round(student_score)
if student_score >=80 <=100:
    print("you got an A")
elif student_score >=70 <=79:
    print("you got a B")
elif student_score >=60 <=69:
    print("you got a C")
elif student_score >=50 <=59:
    print("you got a D")    
elif student_score >=40 <=49:
    print("you got a E")    
else:
    print("you got an F")    