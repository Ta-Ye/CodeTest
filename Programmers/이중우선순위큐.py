import heapq
def solution(operations):
    check_min=[]
    check_max=[]
    for oper in operations:
        if oper=="D 1":
            if check_max:
                heapq.heappop(check_max)
                check_min=[-i for i in check_max]
                heapq.heapify(check_min)
        elif oper=="D -1":
            if check_min:
                heapq.heappop(check_min)
                check_max=[-i for i in check_min]
                heapq.heapify(check_max)
        else:
            num=int(oper.split()[1])
            heapq.heappush(check_min,num)
            heapq.heappush(check_max,-num)
    
    return [-heapq.heappop(check_max),heapq.heappop(check_min)]if check_min and check_max else [0,0]
