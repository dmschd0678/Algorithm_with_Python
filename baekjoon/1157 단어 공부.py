word = input().upper()
l = list(set(word))
cnt = []
for i in l:
    cnt.append(word.count(i))

print(str(l[cnt.index(max(cnt))]).upper() if cnt.count(max(cnt)) == 1 else "?")