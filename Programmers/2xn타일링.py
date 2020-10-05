def solution(n):
    if n<=2:
        return n
    
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    
    for i in range(3,n+1):
        a,dp[i]=divmod(dp[i-1]+dp[i-2],1000000007)
        
    return dp[n]
