def solution(A, K):
    N = len(A)
    B = [None] * N
    #print(f'This is the length of Array: {N}')
    #print(B)
    for i in range(0,N):
        B[(i+K)%N] = A[i]
        #print(B)
    return B

def solution2(A,K):
    if len(A) == 0:
        return A
    else:
        K %= len(A)
        return A[-K:] + A[:-K]

A = [3, 8, 9, 7, 6]
K = 2

print(solution2(A, K))