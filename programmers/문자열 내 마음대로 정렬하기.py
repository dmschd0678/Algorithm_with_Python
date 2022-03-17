def solution(strings, n):
    strings.sort(key = lambda strings : (strings[n], strings))
    return strings