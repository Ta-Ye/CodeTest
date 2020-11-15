def solution(strs, t):
    strs=[[i for i in strs if len(i)==j] for j in range(1,6)]
    dp=[10**8]*(len(t))

    for idx in range(5): # 5개까지
        if t[:idx+1] in strs[idx]:
            dp[idx]=1
            continue
        for i in range(idx):
            if t[idx-i:idx+1] in strs[i]: # 1개
                dp[idx]=min(dp[idx-i-1]+1,dp[idx])
    
    for idx in range(5,len(t)):
        for i in range(5):
            if t[idx-i:idx+1] in strs[i]:
                dp[idx]=min(dp[idx-i-1]+1,dp[idx])
                
    return dp[-1] if dp[-1]!=10**8 else -1
