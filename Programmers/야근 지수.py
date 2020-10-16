import heapq
def solution(n, works):
    if sum(works)<=n:
        return 0
    works=[-i for i in works]
    heapq.heapify(works)
    
    for _ in range(n):
        ck=heapq.heappop(works)
        heapq.heappush(works,ck+1)
        
    return sum([i**2 for i in works])
