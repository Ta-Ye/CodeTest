def solution(people, limit):
    answer=0
    people.sort()
    start=ck=0
    end=len(people)-1
    while start<end:
        if people[start]+people[end]>limit:
            end-=1
            answer+=1
        elif people[start]+people[end]<limit:
            people[end]+=people[start]
            start+=1
        else:
            start+=1
            end-=1
            answer+=1
    return answer if start!=end else answer+1
