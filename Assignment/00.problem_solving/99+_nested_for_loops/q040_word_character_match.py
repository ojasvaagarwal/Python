s = input("Enter keys: ").split()
result = []
for i in s:
    for j in s:
        if i!=j and [j,i] not in result:
            for m in i:
                for n in j:
                    if m==n and [i,j] not in result:
                        result.append([i,j])
                        print(i,j)
                        break