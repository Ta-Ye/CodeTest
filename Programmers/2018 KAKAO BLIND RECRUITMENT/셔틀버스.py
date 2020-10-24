def solution(n, t, m, timetable):
    table,label=dict(),[]
    for idx in range(n):
        table[540+idx*t]=[]
        label.append(540+idx*t)
    
    for time in sorted(timetable):
        hour,minute=time.split(':')
        for bus in table:
            if len(table[bus])<m and bus>=int(hour)*60+int(minute):
                table[bus].append(int(hour)*60+int(minute))
                break
    
    answer= table[label[-1]][-1]-1 if len(table[label[-1]])==m else label[-1]   
    return str(answer//60).zfill(2)+':'+str(answer%60).zfill(2)
