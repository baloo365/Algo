word = list(input().rstrip())
# print(word)
dict = {}
for i in word:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
# print(dict)

# 답이 여러개일 경우 사전 순으로 앞서는 것을 출력한다.
# 1종류까지 홀수 허락
cnt = 0
odd = ''
result = ''
for a in sorted(dict):
    # 홀수일 경우
    if dict[a] % 2 == 1:
        cnt += 1
        if cnt == 1:
            odd = a
        else:
            result = "I'm Sorry Hansoo"
            break
        # print(a)
    # 그외
    dict[a] = (dict[a] // 2)
    result += (a*dict[a])

# print(odd)

if result != "I'm Sorry Hansoo":
    if cnt == 1:
        result = result + odd + result[::-1]
    else:
        result = result + result[::-1]
print(result)
