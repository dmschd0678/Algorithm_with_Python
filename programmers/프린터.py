def solution(priorities, location):
    answer = 0
    l = [0] * len(priorities)
    l[location] = 1

    while True:
        if max(priorities) == priorities[0]:
            answer += 1
            if l[0] == 1:
                break
            priorities.pop(0)
            l.pop(0)
        else:
            l.append(l.pop(0))
            priorities.append(priorities.pop(0))

    return answer

print(solution([4,2,1,9,5,2], 2))