import re
def solution(m, musicinfos):
    answer=[]
    f=re.compile("([A-Z])(\#)?")
    m=[x+y for x,y in f.findall(m)]
    musicinfos=[i.split(',') for i in musicinfos]
    for start,end,name,music in musicinfos:
        start,end=start.split(":"),end.split(":")
        time=60*(int(end[0])-int(start[0]))+int(end[1])-int(start[1])
        music=[x+y for x,y in f.findall(music)]
        new_music=[music[idx%len(music)] for idx in range(time)]
        for idx in range(len(new_music)):
            if m==new_music[idx:idx+len(m)]:
                answer.append([time,name])
                break
    return sorted(answer,key=lambda x: -x[0])[0][1] if answer else '(None)'
