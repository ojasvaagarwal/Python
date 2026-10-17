def calculate_result(marks, passing_marks=35):
    if marks>=passing_marks:return "pass"
    return "fail"
print(calculate_result(55))
print(calculate_result(55,1000))