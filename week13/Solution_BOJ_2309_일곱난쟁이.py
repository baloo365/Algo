N = 9
nanjaeng = [int(input()) for _ in range(N)]
total = sum(nanjaeng)
remove1, remove2 = 0, 0

for i in range(N):
    for j in range(i+1, N):
        if total - nanjaeng[i] - nanjaeng[j] == 100:
            remove1 = nanjaeng[i]
            remove2 = nanjaeng[j]
            break

nanjaeng.remove(remove1)
nanjaeng.remove(remove2)
nanjaeng.sort()
print('\n'.join(map(str, nanjaeng)))
