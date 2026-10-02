even_count = 0
odd_count = 0
positive_count = 0
negative_count = 0
zero_count = 0
largest_number = 0
highest = -9223372036854775808
matrix = ""

for i in range(1,4):
    matrix_row = ""
    for j in range(1,4):
        aij = int(input(f"Enter number for m = {i} and n = {j} in given empty matrix: "))
        if aij%2 == 0:
            even_count+=1
        else:
            odd_count+=1
        if aij == 0:
            zero_count+=1
        elif aij > 0:
            positive_count+=1
        else:
            negative_count+=1
        if aij > highest:
            highest = aij
        aij = str(aij)
        matrix_row = matrix_row+" "+aij
    matrix = matrix + matrix_row + "\n" 
print(matrix)
print(f"""Even count : {even_count}
Odd count : {odd_count}
Positive count : {positive_count}
Negative count : {negative_count}
Zero count : {zero_count}
Largest number : {highest}""")