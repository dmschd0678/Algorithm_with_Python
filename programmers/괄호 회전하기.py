def solution(s):
    answer = 0
    check = True
    for _ in range(len(s)):
        l = []
        s = s[1:] + s[0]
        for i in range(len(s)):
            try:
                if s[i] in ["[","{","("]:
                    l.append(s[i])
                elif s[i] == "]":
                    if l[-1] == "[":
                        l.pop(-1)
                elif s[i] == "}":
                    if l[-1] == "{":
                        l.pop(-1)
                elif s[i] == ")":
                    if l[-1] == "(":
                        l.pop(-1)
            except:
                check = False
                break
        if not l and check:
            answer += 1
        check = True
    return answer

p = ["}]()[{","[](){}"]
for i in p:
    print(solution(i))