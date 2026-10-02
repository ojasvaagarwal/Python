even_count = 0
odd_count = 0
matrix = ""
pri_num = sec_num = 0
for i in range(1,5):
    matrix_row = ""
    for j in range(1,5):
        aij = int(input(f"Enter number for m = {i} and n = {j} in given empty matrix: "))
        if i == j:
            if aij%2 == 0:
                even_count+=1
            pri_num+=aij
        elif i + j == 5:
            if aij%2 != 0:
                odd_count+=1
            sec_num+=aij
        aij = str(aij)
        matrix_row = matrix_row+" "+aij
    matrix = matrix + matrix_row + "\n" 
print(matrix)
print(f"""
Main diagonal sum. : {pri_num}
Secondary diagonal sum. : {sec_num}
Number of even values on the main diagonal. : {even_count}
Number of odd values on the secondary diagonal. : {odd_count}
""")