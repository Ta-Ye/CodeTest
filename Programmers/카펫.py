def solution(brown, yellow):
    width=yellow
    height=1
    while width>=height:
        if (width+2)*(height+2)-width*height==brown:
            return [width+2,height+2]
        else:
            while width>=height:
                height+=1
                if yellow%(height)==0:
                    width=yellow//(height)
                    break
