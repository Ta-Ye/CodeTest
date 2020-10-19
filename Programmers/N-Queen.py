answer=0
def queen(num,board):
    global answer
    if num==len(board):
        answer+=1
        return
    
    for x in range(1,len(board)+1):
        if x in board[:num]:
            continue
        for i in range(1,num+1):
            if abs(x-board[num-i])==i:
                break
        else:
            board[num]=x
            queen(num+1,board)
            board[num]=0
            
def solution(n):
    queen(0,[0]*n)
    return answer
