def solution(bridge_length, weight, truck_weights):
    answer = 0
    N=len(truck_weights)
    end,going=[],[0]*bridge_length
    while len(end)!=N:
        ck=going.pop(0)
        if ck:
            end.append(ck)
        if truck_weights:
            if sum(going)+truck_weights[-1]<=weight:
                going.append(truck_weights.pop())
            else:
                going.append(0)
        else:
            going.append(0)
        answer+=1
    return answer
