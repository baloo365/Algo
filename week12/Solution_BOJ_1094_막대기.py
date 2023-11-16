X = int(input())

def stick(num):
    mok = num // 2
    nameoji = num % 2
    if num <= 1:
        return num

    return stick(mok) + nameoji

print(stick(X))
