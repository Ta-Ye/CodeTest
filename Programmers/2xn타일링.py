def solution(n):
    check=[[] for _ in range(n+1)]
    if n<=3:
        return n
    check[1]=[[1]]
    check[2]=[[1,1],[2]]
    check[3]=[[1,2],[2,1],[1,1,1]]
    
    for idx in range(4,n+1):
        for i in range(1,idx):
            for ck1 in check[i]:
                for ck2 in check[idx-i]:
                    ans=ck1+ck2
                    if not ans in check[idx]:
                        check[idx].append(ans)
    return len(check[idx])
