import queue
def solution(N, road, K):
    length=[1000000]*(N+1)
    length[1]=0
    road_dict=dict()
    for start,end,leng in road:
        if start in road_dict:
            road_dict[start].append([end,leng])
        else:
            road_dict[start]=[[end,leng]]
        if end in road_dict:
            road_dict[end].append([start,leng])
        else:
            road_dict[end]=[[start,leng]]
    q=queue.Queue()
    q.put(1)
    while q.qsize():
        start=q.get()
        for end,cost in road_dict[start]:
            if length[end]>length[start]+cost:
                length[end]=length[start]+cost
                q.put(end)
    
    answer=0
    for i in length[1:]:
        if i <=K:
            answer+=1
    return answer
