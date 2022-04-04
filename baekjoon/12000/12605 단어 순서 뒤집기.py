n = int(input())

l = []

for i in range(n):
    word = input().split()[::-1]
    l.append(word)
cnt = 0
for i in l:
    cnt += 1
    print(f"Case #{cnt}:", end= " ")
    for j in range(len(i)):
        print(i[j], end = " ")
    print()