from itertools import permutations
def calcul(expression,num,oper):
    if num==3:
        return expression
    cp=expression.split(oper[num])
    cp=[calcul(i,num+1,oper) for i in cp]
    return str(eval(oper[num].join(cp)))

def solution(expression):
    answer=0
    for oper in permutations(['+','-','*'],3):
        answer=max(answer,abs(int(calcul(expression,0,oper))))
    return answer
