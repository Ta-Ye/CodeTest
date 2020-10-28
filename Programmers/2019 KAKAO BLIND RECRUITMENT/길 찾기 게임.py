import sys
sys.setrecursionlimit(10**9)
class Node:
    def __init__(self,num):
        self.num=num
        self.left=None
        self.right=None

def create(nodeinfo):
    nodeinfo.sort(key=lambda x: (x[2],x[1]))
    num,x,y=nodeinfo.pop()
    new_Node=Node(num)
    
    left,right=[],[]
    for idx in range(len(nodeinfo)):
        if nodeinfo[idx][1]>x:
            right.append(nodeinfo[idx])
        else:
            left.append(nodeinfo[idx])
    
    if left:
        new_Node.left=create(left)
    if right:
        new_Node.right=create(right)
    return new_Node

def preorder(node,answer):
    answer.append(node.num)
    if node.left:
        preorder(node.left,answer)
    if node.right:
        preorder(node.right,answer)
    return answer

def postorder(node,answer):
    if node.left:
        postorder(node.left,answer)
    if node.right:
        postorder(node.right,answer)
    answer.append(node.num)
    return answer

def solution(nodeinfo):
    nodeinfo=[[idx+1]+i for idx,i in enumerate(nodeinfo)]
    node=create(nodeinfo)
    return[preorder(node,[]),backorder(node,[])]
