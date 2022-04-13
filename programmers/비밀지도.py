def solution(n, arr1, arr2):
    answer = []

    map = list(arr1[i] | arr2[i]for i in range(n))

    for i in range(n):
        line = ""
        for j in bin(map[i])[2:].zfill(n):
            if j == "1":
                line += ("#")
            else:
                line+=(" ")
        answer.append(line)

    return answer

print(solution(6, [46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))