def solution(record):
    answer=[]
    name=dict()
    for s in record:
        s=s.split()
        if s[0]=='Enter':
            answer.append([s[1],'님이 들어왔습니다.'])
            name[s[1]]=s[2]
        elif s[0]=='Leave':
            answer.append([s[1],'님이 나갔습니다.'])
        elif s[0]=='Change':
            name[s[1]]=s[2]
    
    return [name[i]+j for i,j in answer]
