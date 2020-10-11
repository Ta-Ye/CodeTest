def solution(distance, rocks, n):
    rocks=[0]+sorted(rocks)+[distance]
    length=[rocks[i+1]-rocks[i] for i in range(len(rocks)-1)]
    start,end=0,distance
    while start<=end:
        middle=(start+end)//2
        cnt=0
        new_length=[i for i in length]
        for here in range(len(new_length)):
            if new_length[here]<middle:
                if here<len(new_length)-1:
                    new_length[here+1]+=new_length[here]
                cnt+=1
        if cnt>n:
            end=middle-1
        else:
            start=middle+1
    
    return end
