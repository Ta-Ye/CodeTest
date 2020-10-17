def solution(numbers, hand):
    answer = ''
    key=dict()
    key[0],key[1],key[2],key[3],key[4],key[5],key[6],key[7],key[8],key[9]=[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]
    left,right=[3,0],[3,2]
    
    for number in numbers:
        if number==1 or number==4 or number==7:
            answer+='L'
            left=key[number]
        elif number==3 or number==6 or number==9:
            answer+='R'
            right=key[number]
        elif abs(key[number][0]-left[0])+abs(key[number][1]-left[1])>abs(key[number][0]-right[0])+abs(key[number][1]-right[1]):
            answer+='R'
            right=key[number]
        elif abs(key[number][0]-left[0])+abs(key[number][1]-left[1])<abs(key[number][0]-right[0])+abs(key[number][1]-right[1]):
            answer+='L'
            left=key[number]
        else:
            if hand=="right":
                answer+='R'
                right=key[number]
            else:
                answer+='L'
                left=key[number]
    return answer
