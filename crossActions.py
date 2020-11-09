# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 03:20:38 2020

@author: Prthamesh
"""
def checkFaceForWhiteEdge(face):
    if (face[0][1] == 'w' or
        face[1][0] == 'w' or
        face[1][2] == 'w' or
        face[2][1] == 'w'
        ): return True
    return False

# returns True if it has white edge
def checkFrontLayer(wf,gf,of,bf,rf,yf):
    #wf,gf,of,bf,rf,yf = state
    if (yf[2][1]=='w' or
        of[1][0]=='w' or
        wf[0][1]=='w' or
        rf[1][2]=='w' or
        checkFaceForWhiteEdge(gf)
        ):
        return True
    return False

# returns True if it has white edge
def checkBackLayer(wf,gf,of,bf,rf,yf):
    #wf,gf,of,bf,rf,yf = state
    if (yf[0][1]=='w' or
        of[1][2]=='w' or
        wf[2][1]=='w' or
        rf[1][0]=='w' or
        checkFaceForWhiteEdge(bf)
        ):
        return True
    return False

# returns True if it has white edge
def checkLeftLayer(wf,gf,of,bf,rf,yf):
    #wf,gf,of,bf,rf,yf = state
    if (yf[1][0]=='w' or
        gf[1][0]=='w' or
        wf[1][0]=='w' or
        bf[1][2]=='w' or
        checkFaceForWhiteEdge(rf)
        ):
        return True
    return False

# returns True if it has white edge
def checkRightLayer(wf,gf,of,bf,rf,yf):
    #wf,gf,of,bf,rf,yf = state
    if (yf[1][2]=='w' or
        gf[1][2]=='w' or
        wf[1][2]=='w' or
        bf[1][0]=='w' or
        checkFaceForWhiteEdge(of)
        ):
        return True
    return False

# returns True if it has white edge
def checkUpLayer(wf,gf,of,bf,rf,yf):
    #wf,gf,of,bf,rf,yf = state
    if (gf[0][1]=='w' or
        of[0][1]=='w' or
        bf[0][1]=='w' or
        rf[0][1]=='w' or
        checkFaceForWhiteEdge(yf)
        ):
        return True
    return False

# returns True if it has white edge
def checkDownLayer(wf,gf,of,bf,rf,yf):
    #wf,gf,of,bf,rf,yf = state
    if (gf[2][1]=='w' or
        of[2][1]=='w' or
        bf[2][1]=='w' or
        rf[2][1]=='w' or
        checkFaceForWhiteEdge(wf)
        ):
        return True
    return False
    

# If a move does not change any white position, then its an unnecessary move
def checkBlankMove(state): 
    blankMoveList = ['R','L','F','B','U','D']
    wf,gf,of,bf,rf,yf = state
    
    if checkFrontLayer(wf,gf,of,bf,rf,yf): blankMoveList.remove('F')
    if checkBackLayer(wf,gf,of,bf,rf,yf): blankMoveList.remove('B')
    if checkLeftLayer(wf,gf,of,bf,rf,yf): blankMoveList.remove('L')
    if checkRightLayer(wf,gf,of,bf,rf,yf): blankMoveList.remove('R')
    if checkUpLayer(wf,gf,of,bf,rf,yf): blankMoveList.remove('U')
    if checkDownLayer(wf,gf,of,bf,rf,yf): blankMoveList.remove('D')
    
    if blankMoveList:
        return blankMoveList[0]
    else:
        return None

def getAvailableActions(prev1,prev2,state):
    
    availableActions = ["R1","R2","R'",
           "U1","U2","U'",
           "F1","F2","F'",
           "D1","D2","D'",
           "L1","L2","L'",
           "B1","B2","B'",
           ]
    
    if prev1[0] == 'R': 
        availableActions = [action for action in availableActions if action[0]!='R']
        if prev2[0] == 'L': 
            availableActions = [action for action in availableActions if action[0]!='L']
    elif prev1[0] == 'L': 
        availableActions = [action for action in availableActions if action[0]!='L']
        if prev2[0] == 'R': 
            availableActions = [action for action in availableActions if action[0]!='R']
    elif prev1[0] == 'U': 
        availableActions = [action for action in availableActions if action[0]!='U']
        if prev2[0] == 'D': 
            availableActions = [action for action in availableActions if action[0]!='D']
    elif prev1[0] == 'D': 
        availableActions = [action for action in availableActions if action[0]!='D']
        if prev2[0] == 'U': 
            availableActions = [action for action in availableActions if action[0]!='U']
    elif prev1[0] == 'F': 
        availableActions = [action for action in availableActions if action[0]!='F']
        if prev2[0] == 'B': 
            availableActions = [action for action in availableActions if action[0]!='B']
    elif prev1[0] == 'B': 
        availableActions = [action for action in availableActions if action[0]!='B']
        if prev2[0] == 'F': 
            availableActions = [action for action in availableActions if action[0]!='F']
    
    blankMove = checkBlankMove(state)
    availableActions = [action for action in availableActions if action[0]!=blankMove]
    return availableActions