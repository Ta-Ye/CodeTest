answer=[]
def hanoi(x,y,z,num):
    if num==1:
        answer.append([x,y])
        return
    
    hanoi(x,z,y,num-1)
    hanoi(x,y,z,1)
    hanoi(z,y,x,num-1)
    
def solution(n):
    hanoi(1,3,2,n)
    return answer
