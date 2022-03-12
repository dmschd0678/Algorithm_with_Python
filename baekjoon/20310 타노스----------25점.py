word = input()

zero = word.count("0")
one = word.count("1")

print("0" * (zero // 2) + "1" * (one // 2))