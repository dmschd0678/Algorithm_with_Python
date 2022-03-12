aeiou = ['a','e','i','o','u']

while True:
    s = input()

    if s == '#': break

    cnt = 0

    for i in aeiou:
        cnt +=s.count(i)
        cnt += s.count(i.upper())
    print(cnt)