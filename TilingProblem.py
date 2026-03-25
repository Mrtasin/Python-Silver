
def tilingProblem(n):
    if n <= 2:
        return n
    
    if n in dp:
        return dp[n]

    dp[n] = (tilingProblem(n-1) + tilingProblem(n-2))
    return dp[n]


dp = {}


print(tilingProblem(int(input("Enter a number : "))))
