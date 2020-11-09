# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:53:03 2020

@author: Prthamesh
"""
import ActionResults

acd = {"1":1,"2":2,"'":3} # action count dictionary

def getTheCase(state):
    wf,gf,of,bf,rf,yf = state
    l = [rf[0],gf[0],of[0],bf[0]]
    s1 = yf[0][0]+yf[1][0]+yf[2][0]+yf[2][1]+yf[2][2]+yf[1][2]+yf[0][2]+yf[0][1]
    s2 = ''
    for row in l:
        for i in range(3):
            s2 = s2 + row[i]
    caseKey = s1+","+s2
    tempCaseKey = ''
    for letter in caseKey:
        if letter == 'y' or letter == ',':
            tempCaseKey += letter
        else:
            tempCaseKey += 'n'
    caseKey = tempCaseKey
    return caseKey
    
def executeActionSequence(state,actionSequence):
    for action in actionSequence:
        count = acd[action[1]]
        if action[0] == 'L':
            state = ActionResults.leftAction(state,count)
        elif action[0] == 'R':
            state = ActionResults.rightAction(state,count)
        elif action[0] == 'U':
            state = ActionResults.upAction(state,count)
        elif action[0] == 'D':
            state = ActionResults.downAction(state,count)
        elif action[0] == 'F':
            state = ActionResults.frontAction(state,count)
        elif action[0] == 'B':
            state = ActionResults.backAction(state,count)
    return state
