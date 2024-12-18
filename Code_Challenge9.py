for v in range(1, 6):
    for w in range(1, v + 1):
        print(" ", end=" ")
    for x in range(6, v, -1):
        print("*", end=" ")
    print()