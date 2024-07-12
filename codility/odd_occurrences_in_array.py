def solution(A):
    result = 0
    for i in A:
        result ^= i
        print(result)
    return result

A = [9, 3, 9, 3, 9, 7, 9]

print(solution(A))