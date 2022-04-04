# import sys
#
# n = sys.stdin.readline()[:-1]
# n = n[::-1]
#
# num = 0
# for i in range(len(n)):
#     num += int(n[i]) * (8 ** i)
#
# print(bin(num)[2:])

n = int('0o' + input(),8)
print(bin(n)[2:])