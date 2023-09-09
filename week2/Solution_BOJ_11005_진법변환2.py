def f(number, bit):
    if number < bit:
        if number >= 10:
            number = dict[number]
            return number
        else:
            return str(number)
    mok = number // bit     # 몫
    nameoji = number % bit     # 나머지
    if nameoji >= 10:
        nameoji = dict[nameoji]
        return result + f(mok, bit) + nameoji
    else:
        return result + f(mok, bit) + str(nameoji)

number, bit = map(int, input().split())
result = ''
dict = {
}
for i in range(10, 36):
    dict[i] = chr(i+55)

print(f(number, bit))
