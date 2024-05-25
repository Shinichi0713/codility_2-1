def solution(A, K):
    if len(A) == 0:
        return A
    else:
        for i in range(K):
            number_poped = A.pop(-1)
            A.insert(0, number_poped)
        return A