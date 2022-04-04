num =  input().split()

num = [int(i) for i in num]
if num[0] > num[1]:
    print(">")
elif num[0] < num[1]:
    print("<")
elif num[0] == num[1]:
    print("==")