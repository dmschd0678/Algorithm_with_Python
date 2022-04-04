import sys

n = int(sys.stdin.readline())

people = []

for _ in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    people.append((age, name))

people.sort(key = lambda x: x[0])

for age,name in people:
    print(int(age),name)