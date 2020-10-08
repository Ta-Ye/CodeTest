import queue
def solution(n, computers):
    answer=0
    q=queue.Queue()
    check=[0]*n
    for num in range(n):
        if check[num]:
            continue
        q.put(num)
        while q.qsize():
            ck=q.get()
            check[ck]=1
            for idx,com in enumerate(computers[ck]):
                if com==1 and check[idx]==0:
                    q.put(idx)
        answer+=1
    return answer
