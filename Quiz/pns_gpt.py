import math
import copy
import time
from game_basics import EMPTY, BLACK, WHITE, opponent
# class Node:
#     def __init__(self, value=None, type=None, parent=None, children=None, expanded=False, proof=None, disproof=None):
#         self.value = value
#         self.type = type
#         self.parent = parent
#         self.children = children or []
#         self.expanded = expanded
#         self.proof = proof
#         self.disproof = disproof

def PNS(root):
    print("root:   ")
    root.print()
    if root.toPlay == BLACK:
        root.type = "OR"
    else:
        root.type = "AND"
    Evaluate(root)
    
    SetProofAndDisproofNumbers(root)
    print("value of the root\n", root.value, root.type, root.proof, root.disproof)
    current = copy.deepcopy(root)
    most_proving = copy.copy(root)
    print("current and mpn", current.print(), most_proving.print())
    c = 0
    while root.proof != 0 and root.disproof != 0:
        print("times while loop ", c)
        c = c+1
        most_proving = SelectMostProvingNode(current)
        print("most proving node", most_proving.print())
        ExpandNode(most_proving)
        print("Expand node true or false", most_proving.expanded)
        current = UpdateAncestors(most_proving, root)
        print("current node",current.print())
    if root.proof == 0:
        print("Black is win")

    else:
        print("White is win")
def Evaluate(node):

    if node.proof is None or node.disproof is None:
        node.value = "unknown"
        return

    if node.proof == 0:
        node.value == "proven"

    elif node.disproof == 0:
        node.value == "disproven"

    else:
        node.value = "unknown"

def SetProofAndDisproofNumbers(node):
    if node.expanded:
        if node.type == "AND":
            node.proof = 0
            node.disproof = math.inf
            for child in node.children:
                node.proof += child.proof
                node.disproof = min(node.disproof, child.disproof)
        else:
            node.proof = math.inf
            node.disproof = 0
            for child in node.children:
                node.disproof += child.disproof
                node.proof = min(node.proof, child.proof)
    else:
        if node.value == "disproven":
            node.proof = math.inf
            node.disproof = 0
        elif node.value == "proven":
            node.proof = 0
            node.disproof = math.inf
        else:
            node.proof = 1
            node.disproof = 1

def SelectMostProvingNode(node):
    
    best = None
    while node.expanded:
        value = math.inf
        if node.type == "OR":
            for child in node.children:
                if value > child.proof:
                    best = child
                    value = child.proof
        else:
            for child in node.children:
                if value > child.disproof:
                    best = child
                    value = child.disproof
        node = best
    return node

def ExpandNode(node):
    GenerateChildren(node)
    for i in range(len(node.children)):
        
        child = node.children[i]
        print(i,"child of node ", node.print(), "children", child.print())
        child.parent = node
        if child.toPlay == BLACK:
            child.type = "OR"
        else:
            child.type = "AND"
        Evaluate(child)
        SetProofAndDisproofNumbers(child)
        print(i, "value of the child\n = ", child.value, child.type, child.proof, child.disproof)
        if (node.type == "OR" and child.proof == 0) or (node.type == "AND" and child.disproof == 0):
            break
    node.expanded = True

def GenerateChildren(node):
    for m in node.legalMoves():
        node.play(m)
        node.children.append(copy.copy(node)) # memory 
        node.undoMove()
    # Implement this function to generate children for node
  #  pass

def UpdateAncestors(node, root):
    while True:
        print("node i.e. current\n")
        node.print()
        print("root\n", root.print())
        old_proof = node.proof
        old_disproof = node.disproof
        print("old pn and dn for node ", old_proof, old_disproof)
        SetProofAndDisproofNumbers(node)
        print("current pn and dn for node ", node.proof, node.disproof)
        if node.proof == old_proof and node.disproof == old_disproof:
            print("old and new pn, dn same\n")
            return node
        if node == root:
            print("root and node same\n")
            return node
        node = node.parent
        print("looping now and parent\n", node)
