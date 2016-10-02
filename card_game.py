# A: input array
# i: left index
# j: right index
maxSumAnswers = {}
def maxSum(A, i, j):
    if (i, j) in maxSumAnswers:
        return maxSumAnswers[(i, j)]

    if j - i <= 1:
        ans = max(A[i:j+1])
        maxSumAnswers[(i,j)] = ans
        return ans
    
    # 1 2 2 3 1 1
    # maxSum(A, i, j) = max(
    #                        A[i] + min(maxSum(A, i+2, j), maxSum(A, i+1, j-1)), 
    #                        A[j] + min(maxSum(A, i+1, j-1), maxSum(A, i, j-2))
    #                      )
    
    maxSum1 = maxSum(A, i+2, j)
    maxSum2 = maxSum(A, i+1, j-1)
    maxSum3 = maxSum(A, i, j-2)

    ans = max(A[i] + min(maxSum1, maxSum2), A[j] + min(maxSum2, maxSum3))
    maxSumAnswers[(i,j)] = ans
    return ans

A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 1, 1, 1]
ans = maxSum(A, 0, len(A) - 1)
print(ans)
