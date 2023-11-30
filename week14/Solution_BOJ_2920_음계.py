lists = list(map(int, input().split()))

if lists == sorted(lists):
    print("ascending")
elif lists == sorted(lists, reverse=True):
    print("descending")
else:
    print("mixed")
