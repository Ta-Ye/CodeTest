def solution(triangle):
    dp=[[0]*i for i in range(1,len(triangle)+1)]
    dp[0][0]=triangle[0][0]
    for x in range(1,len(dp)):
        dp[x][0]=triangle[x][0]+dp[x-1][0]
        dp[x][-1]=triangle[x][-1]+dp[x-1][-1]
    
    for x in range(2,len(dp)):
        for y in range(1,len(dp[x])-1):
            dp[x][y]=triangle[x][y]+max(dp[x-1][y-1],dp[x-1][y])
    
    return max(dp[-1])
