def Grade_calc(percentage):
    if percentage>=90:
        return "A+"
    if percentage>=80:
        return "A"
    if percentage>=75:
        return "B+"
    if percentage>=70:
        return "B"
    if percentage>=60:
        return "C"
    if percentage>=50:
        return "D"
    else:
        return "F"

def Student_Grade_Calculator():
    print("Student grade calculator")

    marks=[]
    for i in range(1,6):
        mark=float(input(f"Enter marks for the subject {1} (out of 100):  "))
        marks.append(mark)

    total=sum(marks)
    percentage = total/5
    grade= Grade_calc(percentage)

    print("Report: ")
    print(f" Total marks {total}/500")
    print(f" Percentage {percentage}")
    print(f" GRADE : {grade}")

    if grade=="F":
        print("FAIL")
    else:
        print("Congratulations")

Student_Grade_Calculator()
    

          
    
