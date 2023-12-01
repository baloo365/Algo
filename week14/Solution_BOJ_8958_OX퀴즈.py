T = int(input())

for i in range(T):
    row_list = list(input())
    sum2 = 1
    result = 0
    for i in range(len(row_list)):
        if row_list[i] == "O":
            result +=sum2
            sum2 +=1
        else:
            sum2 = 1
            continue
    print(result)
