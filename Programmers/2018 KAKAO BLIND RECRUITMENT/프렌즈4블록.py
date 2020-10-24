def solution(m, n, board):
    answer=0
    new_board=[[] for _ in range(n)]
    for y in range(n):
        for x in range(m-1,-1,-1):
            new_board[y].append(board[x][y])
    board=new_board
    
    while True:
        ck=[]
        for x in range(n-1):
            for y in range(m-1):
                if board[x][y]=='[':
                    continue
                if len(set([board[x][y],board[x+1][y],board[x][y+1],board[x+1][y+1]]))==1:
                    ck+=[(x,y),(x+1,y),(x,y+1),(x+1,y+1)]
        ck=list(set(ck))
        if len(ck)==0:
            return answer
        answer+=len(ck)
        for x,y in ck:
            board[x][y]='['
        
        new_board=[[] for _ in range(n)]
        for x in range(n):
            cnt=0
            for y in range(m):
                if board[x][y]!='[':
                    new_board[x].append(board[x][y])
                else:
                    cnt+=1
            new_board[x]+=['[']*cnt
        board=new_board
