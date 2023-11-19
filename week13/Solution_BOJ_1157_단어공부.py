word = input().upper()
word_list = list(set(word))
alphabet_count = []

for i in word_list:
    alphabet_count.append(word.count(i))

if alphabet_count.count(max(alphabet_count)) >=2 :
    print("?")
else:
    print(word_list[alphabet_count.index(max(alphabet_count))])
