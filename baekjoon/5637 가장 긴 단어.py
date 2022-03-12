import sys

s = sys.stdin

x = ["-","(",")",",","."]
s = list(s)
for i in x:
    s.replace(i,"")

print(s)