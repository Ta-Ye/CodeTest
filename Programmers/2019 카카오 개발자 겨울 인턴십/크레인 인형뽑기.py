def solution(board, moves):
    answer = 0
    bag=[]
    for move in moves:
        for x in range(len(board)):
            if board[x][move-1]:
                bag.append(board[x][move-1])
                board[x][move-1]=0
                break
        if len(bag)>=2 and bag[-1]==bag[-2]:
            bag.pop()
            bag.pop()
            answer+=2
    return answer
