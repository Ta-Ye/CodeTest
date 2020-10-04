def solution(lines):
    answer = 0
    check=[]
    for idx,line in enumerate(lines):
        info=line.split()
        info2=info[1].split(":")
        time1= (int(info[0].split('-')[2])-14)*86400+int(info2[0])*3600+int(info2[1])*60+float(info2[2])
        time2=round(time1+0.001-float(info[2].split("s")[0]),3)
        check.append([time2,time1])
        
    check.sort()
    for x,y in check:
        ans=0
        for ck in check:
            if ck[0]<y+1 and ck[1]>=y:
                ans+=1
        answer=max(answer,ans)
    return answer
