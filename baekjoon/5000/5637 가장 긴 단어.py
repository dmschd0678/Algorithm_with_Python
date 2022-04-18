import sys

st = []

while True:
    st.extend(sys.stdin.readline().split())
    if st[-1] == "E-N-D":
        break

word = []
for i in st:
    temp = ""
    for j in i:
        if j.isalpha() or j == "-":
            temp += j.lower()
    word.append(temp)
print(sorted(word,reverse=True, key = lambda x : len(x))[0].lower())