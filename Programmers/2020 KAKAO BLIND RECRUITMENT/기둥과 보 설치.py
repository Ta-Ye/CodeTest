def check(x,y,a,frame):
    if a: # 보
        if [x,y-1,0] in frame or [x+1,y-1,0] in frame or ([x-1,y,1] in frame and [x+1,y,1] in frame):
            return True
    else: # 기둥
        if y==0 or [x,y-1,0] in frame or [x,y,1] in frame or [x-1,y,1] in frame:
            return True
    return False

def solution(n, build_frame):
    # [x,y,a,b] a=0,1 기둥, 보  b=0,1 삭제, 설치
    frame=[]
    for x,y,a,b in build_frame:
        if b:
            if check(x,y,a,frame):
                frame.append([x,y,a])
        else:
            frame.remove([x,y,a])
            for xx,yy,aa in frame:
                if not check(xx,yy,aa,frame):
                    frame.append([x,y,a])
                    break
    return sorted(frame)
