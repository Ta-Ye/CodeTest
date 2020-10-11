def solution(money):
    if len(money)<=3:
        return max(money)
    
    #첫집 o
    answer1=[0]*len(money)
    answer1[0]=money[0]
    answer1[1]=money[1]
    answer1[2]=money[0]+money[2]
    for num in range(3,len(money)-1):
        answer1[num]=money[num]+max(answer1[num-2],answer1[num-3])
    #첫집 x
    answer2=[0]*len(money)
    answer2[1]=money[1]
    answer2[2]=money[2]
    for num in range(3,len(money)):
        answer2[num]=money[num]+max(answer2[num-2],answer2[num-3])
    
    return max(max(answer1),max(answer2))
