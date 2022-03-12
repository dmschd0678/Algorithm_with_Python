def solution(n, lost, reserve):
    answer = 0

    for i in lost:
        for j in reserve:
            if i == j:
                lost.remove(i)
                reserve.remove(j)

    for i in range(1, n + 1):
        if i in lost:
            for j in range(i - 1, i + 2):
                if j in reserve:
                    reserve.remove(j)
                    lost.remove(i)
                    break
    answer = n - len(lost)
    return answer

print(solution(5,[2,3,4],[3,4,5]))