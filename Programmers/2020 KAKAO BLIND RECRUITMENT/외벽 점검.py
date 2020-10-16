def wall_check(n,weaks,dist,k):
    ck=dist.pop()
    next_w=set()
    for weak in list(weaks):
        for idx,num in enumerate(weak):
            w_list=[i-num for i in weak[idx:]]+[n+i-num for i in weak[:idx]]
            w_list=[i for i in w_list if i>ck]
            if len(w_list)==0:
                return k
            next_w.add(tuple(w_list))
    if len(dist): 
        return wall_check(n,next_w,dist,k+1)
    else:
        return -1
            
def solution(n, weak, dist):
    return wall_check(n,[weak],dist,1)
