N, P, Q = list(map(int, input().split()))

d = {0:1}

def solution(n):
    if n in d.keys():
        return d[n]
    d[n] = solution(n // P) + solution(n // Q)
    return d[n]

print(solution(N))