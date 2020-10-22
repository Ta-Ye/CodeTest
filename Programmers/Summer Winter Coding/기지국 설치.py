def solution(n, stations, w):
    check=[0]
    for station in stations:
        if station-w>0:
            check.append(station-w)
        if station+w<=n:
            check.append(station+w)
    check.append(n+1)
    answer=0
    for i in range(len(check)-1):
        ans,last=divmod(check[i+1]-check[i]-1,2*w+1)
        answer+=ans if last==0 else ans+1
    return answer-len(stations)
