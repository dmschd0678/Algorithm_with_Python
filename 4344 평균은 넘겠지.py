classes = int(input())

for i in range(classes):
    students = input().split()
    students = [int(k) for k in students]
    print("{:.3f}%".format(len([l for l in students[1:] if l > (sum(students[1:]) / (len(students) - 1))]) / (len(students) - 1) * 100))
