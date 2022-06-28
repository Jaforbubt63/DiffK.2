class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        n = len(A)
        i, j = 0, 1
        while i < (n-1) and j < n:
            if i == j:
                j += 1
                continue
            diff = A[j] - A[i]
            if diff == B:
                return 1
            if diff < B:
                j += 1
            else:
                i += 1
        return 0
    