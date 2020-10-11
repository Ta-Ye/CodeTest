def solution(genres, plays):
    answer=[]
    genre=dict()
    for idx, g in enumerate(genres):
        if g in genre:
            genre[g][0].append(idx)
            genre[g][1]+=plays[idx]
        else:
            genre[g]=[[idx],plays[idx]]
            
    ck=sorted(genre,key=lambda x : -genre[x][1])
    for i in ck:
        ans=[(i,plays[i]) for i in genre[i][0]]
        ans.sort(key=lambda x: -x[1])
        answer.append(ans[0][0])
        if len(ans)>=2:
            answer.append(ans[1][0])
    return answer
