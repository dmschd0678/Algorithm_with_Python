while True:
    n = input()

    if n == "0": break

    palin = n[::-1]

    if n == palin:
        print("yes")
    else:
        print("no")