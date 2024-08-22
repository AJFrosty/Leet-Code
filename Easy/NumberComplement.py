# https://leetcode.com/problems/number-complement/description/

def findComplement(num: int) -> int:
    main = []

    while num != 0:
        if num % 2 == 1:
            main.append(1)
            num = num//2
        else:
            main.append(0)
            num = num//2

    main = main[::-1]

    for i in range(len(main)):
        if main[i] == 0:
            main[i] = 1
        else:
            main[i] = 0

    comp = 0
    index = 0
    for j in range(len(main)-1,-1,-1):
        if main[j] == 1:
            comp += 2**index
        index += 1
    return comp
