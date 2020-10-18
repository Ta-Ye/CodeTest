def solution(n, m):
    cp=1
    while True:
        for i in range(2,min(n,m)+1):
            if n%i==0 and m%i==0:
                cp*=i
                n//=i
                m//=i
                break
        else:
            break
    return [cp,n*m*cp]
