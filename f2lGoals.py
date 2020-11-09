# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:27:02 2020

@author: Prthamesh
"""

import crossGoals

def checkFrontRightCorner(cs,es1,es2):
    if (cs[1:] == es1 or cs[1:] == es2):
        return True
    return False

def checkFrontLeftCorner(cs,es1,es2):
    if (cs[1:] == es1 or cs[1:] == es2):
        return True
    return False

def checkBackRightCorner(cs,es1,es2):
    if (cs[1:] == es1 or cs[1:] == es2):
        return True
    return False

def checkBackLeftCorner(cs,es1,es2):
    if (cs[1:] == es1 or cs[1:] == es2):
        return True
    return False

def f2lMatchedPairGoalTest(state,goalFlag):
    wf,gf,of,bf,rf,yf = state
    
    if crossGoals.getCrossCount(state)!=4:
        return (False,0)
    if getInsertedPairCount(state)==4:
        return (True,1)
    count = 1
    if gf[0][2] == 'w':
        cs = 'w' + of[0][0] + yf[2][2] # corner string
        es1 = of[0][1] + yf[1][2] # edge string 1
        es2 = yf[1][0] + rf[0][1] # edge string 2
        if checkFrontRightCorner(cs,es1,es2): return (True,count)
    if of[0][0] == 'w':
        cs = 'w' + gf[0][2] + yf[2][2] # corner string
        es1 = gf[0][1] + yf[2][1] # edge string 1
        es2 = yf[0][1] + bf[0][1] # edge string 2
        if checkFrontRightCorner(cs,es1,es2): return (True,count)
        
    if gf[0][0] == 'w':
        cs = 'w' + rf[0][2] + yf[2][0] # corner string
        es1 = rf[0][1] + yf[1][0] # edge string 1
        es2 = yf[1][2] + of[0][1] # edge string 2
        if checkFrontLeftCorner(cs,es1,es2): return (True,count)
    if rf[0][2] == 'w':
        cs = 'w' + gf[0][0] + yf[2][0] # corner string
        es1 = gf[0][1] + yf[2][1] # edge string 1
        es2 = yf[0][1] + bf[0][1] # edge string 2
        if checkFrontLeftCorner(cs,es1,es2): return (True,count)
        
    if of[0][2] == 'w':
        cs = 'w' + bf[0][0] + yf[0][2] # corner string
        es1 = bf[0][1] + yf[0][1] # edge string 1
        es2 = yf[2][1] + gf[0][1] # edge string 2
        if checkBackRightCorner(cs,es1,es2): return (True,count)
    if bf[0][0] == 'w':
        cs = 'w' + of[0][2] + yf[0][2] # corner string
        es1 = of[0][1] + yf[1][2] # edge string 1
        es2 = yf[1][0] + rf[0][1] # edge string 2
        if checkBackRightCorner(cs,es1,es2): return (True,count)
        
    if rf[0][0] == 'w':
        cs = 'w' + bf[0][2] + yf[0][0] # corner string
        es1 = bf[0][1] + yf[0][1] # edge string 1
        es2 = yf[2][1] + gf[0][1] # edge string 2
        if checkBackLeftCorner(cs,es1,es2): return (True,count)
    if bf[0][2] == 'w':
        cs = 'w' + rf[0][0] + yf[0][0] # corner string
        es1 = rf[0][1] + yf[1][0] # edge string 1
        es2 = yf[1][2] + of[0][1] # edge string 2
        if checkBackLeftCorner(cs,es1,es2): return (True,count)
    return (False,0)

def checkFrontRightInsertedPair(state):
    wf,gf,of,bf,rf,yf = state
    if (wf[0][2]=='w' and 
        gf[1][2]=='g' and
        gf[2][2]=='g' and
        of[1][0]=='o' and
        of[2][0]=='o'): return True
    return False

def checkFrontLeftInsertedPair(state):
    wf,gf,of,bf,rf,yf = state
    if (wf[0][0]=='w' and 
        gf[1][0]=='g' and
        gf[2][0]=='g' and
        rf[1][2]=='r' and
        rf[2][2]=='r'): return True
    return False

def checkBackRightInsertedPair(state):
    wf,gf,of,bf,rf,yf = state
    if (wf[2][2]=='w' and 
        bf[1][0]=='b' and
        bf[2][0]=='b' and
        of[1][2]=='o' and
        of[2][2]=='o'): return True
    return False

def checkBackLeftInsertedPair(state):
    wf,gf,of,bf,rf,yf = state
    if (wf[2][0]=='w' and 
        bf[1][2]=='b' and
        bf[2][2]=='b' and
        rf[1][0]=='r' and
        rf[2][0]=='r'): return True
    return False

def getInsertedPairCount(state):
    wf,gf,of,bf,rf,yf = state
    count = 0
    if checkFrontLeftInsertedPair(state): count += 1
    if checkFrontRightInsertedPair(state): count += 1
    if checkBackRightInsertedPair(state): count += 1
    if checkBackLeftInsertedPair(state): count += 1
    '''
    # Front right
    if (wf[0][2]=='w' and 
        gf[1][2]=='g' and
        gf[2][2]=='g' and
        of[1][0]=='o' and
        of[2][0]=='o'): count += 1
    # Front left
    if (wf[0][0]=='w' and 
        gf[1][0]=='g' and
        gf[2][0]=='g' and
        rf[1][2]=='r' and
        rf[2][2]=='r'): count += 1
    # Back right
    if (wf[2][2]=='w' and 
        bf[1][0]=='b' and
        bf[2][0]=='b' and
        of[1][2]=='o' and
        of[2][2]=='o'): count += 1
    # Back left
    if (wf[2][0]=='w' and 
        bf[1][2]=='b' and
        bf[2][2]=='b' and
        rf[1][0]=='r' and
        rf[2][0]=='r'): count += 1'''
    return count

def f2lInsertedPairGoalTest(state,goalFlag):
    if crossGoals.getCrossCount(state)!=4:
        return (False,0)
    count = getInsertedPairCount(state)
    if count>=goalFlag:
        return (True,count)
    return (False,count)
    