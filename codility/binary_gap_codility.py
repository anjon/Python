def solution(N):
    N = bin(N)[2:]
    print(f'Input Binary Number {N}')
    b = 0
    max_gap = 0

    for i in N:
        if int(i) == 0:
            b += 1
        elif int(i) == 1:
            max_gap = max(b, max_gap)
            b = 0
    print(f'Maximum Binary Gap : {max_gap}')
    return max_gap

print(solution(1041))