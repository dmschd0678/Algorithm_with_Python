def solution(progresses, speeds):
    answer = []
    cnt = 0
    while progresses:
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        if progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            for i in range(len(progresses)):
                if progresses[0] >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    cnt += 1
                else:
                    break
            answer.append(cnt)
            cnt = 0
    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))