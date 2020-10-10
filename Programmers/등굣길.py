def solution(m, n, puddles):
    answer=[[0]*(m+1) for _ in range(n+1)]
    answer[0][1]=1
    for x in range(1,n+1):
        for y in range(1,m+1):
            if not [y,x] in puddles:
                answer[x][y]=(answer[x-1][y]+answer[x][y-1])
    
    return answer[n][m]%1000000007
