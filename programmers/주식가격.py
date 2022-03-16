def solution(prices):
    answer = []

    for i in range(len(prices) - 1):
        cnt = 1
        for j in range(i + 1, len(prices) - 1):
            if prices[i] > prices[j]:
                break
            cnt += 1
        answer.append(cnt)
    answer.append(0)
    return answer

print(solution([1, 2, 3, 2, 3]))