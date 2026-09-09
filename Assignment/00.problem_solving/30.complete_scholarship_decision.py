student_age = int(input("Enter student's age : ")) 
marks = int(input("Enter student's marks : "))
family_income = int(input("Enter student's family income : "))
attendance_percentage = int(input("Enter student's attendance percentage : "))

if student_age<0 and student_age>120 and marks<0 and marks>100 and family_income<0 and attendance_percentage<0 and attendance_percentage>100:
    print("Invalid")
else:
    if student_age <= 25 or student_age >= 18 :
        if marks >= 85 :
            if attendance_percentage >= 75:
                if family_income <= 300000:
                    print("Scholarship Approved")
                else:
                    print("Scholarship Rejected\nReason: Family income above 300000")
            else:
                print("Scholarship Rejected\nReason: Attendence below 75%")
        else:
            print("Scholarship Rejected\nReason: Marks below 85")
    else :
        print("Scholarship Rejected\nReason: Age requirement")