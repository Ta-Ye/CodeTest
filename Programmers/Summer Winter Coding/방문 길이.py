def solution(dirs):
    answer=set()
    x=y=0
    move={'U': [0,1],'D':[0,-1],'R':[1,0],'L':[-1,0]}
    cp={'U': 'D','D':'U','R':'L','L':'R'}
    for d in dirs:
        nx,ny=move[d]
        if x+nx in [-6,6] or y+ny in [-6,6]:
            continue
        answer.add((x,y,cp[d]))
        x,y=x+nx,y+ny
        answer.add((x,y,d))
    return len(answer)//2
