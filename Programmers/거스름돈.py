def solution(n, money):
    dp=[[0]*(n+1) for _ in range(len(money))]
    
    dp[0][0]=1
    for i in range(money[0],n+1,money[0]):
        dp[0][i]=1
    
    for x in range(1,len(money)):
        for y in range(n+1):
            dp[x][y]=dp[x-1][y]+dp[x][y-money[x]] if y>=money[x] else dp[x-1][y]
    
    return dp[-1][-1]
