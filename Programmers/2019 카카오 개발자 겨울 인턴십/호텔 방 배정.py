import sys
sys.setrecursionlimit(10**9)

def recur(num, room):
    room[num]=recur(room[num],room)+1 if num in room else num+1
    return room[num]-1

def solution(k, room_number):
    answer=[]
    room=dict()
    for num in room_number:
        answer.append(recur(num,room))
    return answer
