# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 03:13:33 2020

@author: Prthamesh
"""

def getCrossCount(state):
    wf,gf,of,bf,rf,yf = state
    count = 0
    if (wf[0][1] == 'w' and gf[2][1]=='g'): count += 1
    if (wf[1][0] == 'w' and rf[2][1]=='r'): count += 1
    if (wf[1][2] == 'w' and of[2][1]=='o'): count += 1 
    if (wf[2][1] == 'w' and bf[2][1]=='b'): count += 1
    return count

def goalTest(state,goalFlag):
    count = getCrossCount(state)
    if count>=goalFlag:
        return (True,count)
    return (False,count)


"""def quarterCrossGoalTest(state):
    count = getCrossCount(state)
    if count==1: return (True,count)
    return (False,None)

def halfCrossGoalTest(state):
    count = getCrossCount(state)
    if count==2: return (True,count)
    return (False,None)

def threeQuarterCrossGoalTest(state):
    count = getCrossCount(state)
    if count == 3: return (True,count)
    return (False,None)

def fullCrossGoalTest(state):
    count = getCrossCount(state)
    if count == 4: return (True,count)
    return (False,None)"""