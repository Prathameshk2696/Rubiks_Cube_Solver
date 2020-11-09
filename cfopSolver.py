# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 03:08:26 2020

@author: Prthamesh
"""

# CFOP solver. Sequence of goals
import copy
import crossActions,f2lActions
import ActionResults as ar
import crossGoals,f2lGoals
import oll,ollMapping

acd = {"1":1,"2":2,"'":3} # action count dictionary

def showActionsSequence(actionSequence):
    #print(actionSequence)
    print('\t',end='')
    for action in actionSequence:
        if action[1] == '1': action = action[0]
        print(str(action),end=' ')
    print()

def goalTest(state,stage,goalFlag):
    if stage == 'cross':
        return crossGoals.goalTest(state,goalFlag)
    elif stage == 'f2l_mp': # match pair
        goalFlag = 1
        res = f2lGoals.f2lMatchedPairGoalTest(state,goalFlag)
        #if res: print('True')
        return res
    elif stage == 'f2l_ip': # insert pair
        return f2lGoals.f2lInsertedPairGoalTest(state,goalFlag)
    
def result(state,action):
    a1,a2 = action
    count = acd[a2]
    if a1=='R': state = ar.rightAction(state,count)
    elif a1=='L': state = ar.leftAction(state,count)
    elif a1=='U': state = ar.upAction(state,count)
    elif a1=='D': state = ar.downAction(state,count)
    elif a1=='F': state = ar.frontAction(state,count)
    else: state = ar.backAction(state,count)
    return state

def depthFirstSearch(state,depth,prev1,prev2,stage,goalFlag):
    goalTestRes,count = goalTest(state,stage,goalFlag)
    if goalTestRes: return (True,[],state,count)
    elif depth == 0:return (False,[],None,0)
    else:
        if stage == 'cross':
            availableActions = crossActions.getAvailableActions(prev1,prev2,state)
        elif stage == 'f2l_mp' or stage == 'f2l_ip':
            # prev2 = prev2 + prev1 # sequence of actions so far
            availableActions = f2lActions.getAvailableActions(prev1,prev2,state)
        for action in availableActions:
            res = result(copy.deepcopy(state),action)
            val,soa,ts,count = depthFirstSearch(res,depth-1,action,prev1,stage,goalFlag)
            if val:
                soa = [action] + soa
                return (True,soa,ts,count)
    return (False,[],None,0)

def iterativeDeepeningDepthFirstSearch(state,depth,prev1,prev2,stage,goalFlag):
    val = False
    d = 1
    while d<=depth and not val:#not val:
        #print(stage,d,goalFlag)
        val,actionSequence,ts,count = depthFirstSearch(state,d,prev1,prev2,stage,goalFlag)
        d += 1
    return val,actionSequence,ts,count

def getCrossPrev1Prev2():
    try:
        prev1 = completeActionSequence[-1][-1]
    except IndexError:
        prev1 = '  '
    try:
        prev2 = completeActionSequence[-1][-2]
    except IndexError:
        prev2 = '  '
    return (prev1,prev2)

def checkCrossGoal(state,goalFlag):
    #print(goalFlag)
    val = False
    depth = 4
    stage = 'cross'
    prev1,prev2 = getCrossPrev1Prev2()
    val,actionSequence,ts,count = iterativeDeepeningDepthFirstSearch(state,depth,prev1,prev2,stage,goalFlag)
    showActionsSequence(actionSequence)
    completeActionSequence.append(actionSequence)
    return (val,ts,count)

def tryCrossFrom4To1(state,goalFlag):
    depth = 4
    goalFlag = 4
    stage = 'cross'
    prev1,prev2 = getCrossPrev1Prev2()
    val,actionSequence,ts,count = iterativeDeepeningDepthFirstSearch(state,depth,prev1,prev2,stage,goalFlag)
    showActionsSequence(actionSequence)
    completeActionSequence.append(actionSequence)
    return (ts,count) # return terminal state which becomes initial state for next goal

def doCross(state,goalFlag):
    depth = 4
    stage = 'cross'
    prev1,prev2 = getCrossPrev1Prev2()
    val,actionSequence,ts,count = iterativeDeepeningDepthFirstSearch(state,depth,prev1,prev2,stage,goalFlag)
    showActionsSequence(actionSequence)
    completeActionSequence.append(actionSequence)
    return (ts,count) # return terminal state which becomes initial state for next goal

def completeCross(state):
    count = 0
    print('-'*40)
    print('CROSS : ')
    while(count!=4):
        val = False
        goalFlag = 4
        #(state,count) = doCross(state,count+1)
        while not val:
            (val,state2,count) = checkCrossGoal(state,goalFlag)
            goalFlag -= 1
        state = state2
        #(state,count) = tryCrossFrom4To1(state,count+1)
    #ar.displayState(state)
    return state

def matchPair(state,depth,prev1,prev2,stage,goalFlag):
    val,actionSequence,ts,count = iterativeDeepeningDepthFirstSearch(state,depth,prev1,prev2,stage,goalFlag)
    return val,actionSequence,ts,count

def insertPair(state,depth,prev1,prev2,stage,goalFlag):
    val,actionSequence,ts,count = iterativeDeepeningDepthFirstSearch(state,depth,prev1,prev2,stage,goalFlag)
    return val,actionSequence,ts,count

def doF2L(state,goalFlag):
    depth = 9
    #prev1,prev2 = getF2LPrev1Prev2()
    prev1 = prev2 = '  '
    val,actionSequence,ts,count = matchPair(state,depth,prev1,prev2,'f2l_mp',goalFlag)
    state = ts
    showActionsSequence(actionSequence)
    completeActionSequence.append(actionSequence)
    val,actionSequence,ts,count = insertPair(state,depth,prev1,prev2,'f2l_ip',goalFlag)
    showActionsSequence(actionSequence)
    completeActionSequence.append(actionSequence)
    return (ts,count)

def completeF2L(state):
    f2lActions.initializeNumberOfAllowedMoves()
    count = 0
    print('-'*40)
    print('F2L : ')
    while count!=4:
        (state,count) = doF2L(state,count+1)
    return state

def completeOLL(state):
    wf,gf,of,bf,rf,yf = state
    print('-'*40)
    print('OLL : ')
    caseKey = oll.getTheCase(state)
    #print(caseKey)
    actionSequence = ollMapping.getSequence(caseKey)
    showActionsSequence(actionSequence)
    state = oll.executeActionSequence(state,actionSequence)
    #ar.displayState(state)
    return state

def completePLL(state):
    pass

def beginCFOP(state):
    state = completeCross(state)
    state = completeF2L(state)
    state = completeOLL(state)
    #state = completePLL(state)

def takeInput():
    for faceindex,facename in enumerate(order):
        face = state[faceindex]
        text = 'Enter colors of {} face : '.format(facename)
        s = input(text)
        l = [s[0:3],s[3:6],s[6:9]]
        for i,row in enumerate(l):
            for j,letter in enumerate(row):
                face[i][j] = letter
                
def calculateLengthoOfCompleteActionSequence(cas):
    length = 0
    for actionSequence in cas:
        length += len(actionSequence)
    return length
        
d = dict(w=1,g=2,o=3,b=4,r=5,y=6) # convert letter to number
dAcr = dict(w='wf',g='gf',o='of',b='bf',r='rf',y='yf')
order = ['white','green','orange','blue','red','yellow']

wf = [[None,None,None],
      [None,None,None],
      [None,None,None]]

gf = [[None,None,None],
      [None,None,None],
      [None,None,None]]

of = [[None,None,None],
      [None,None,None],
      [None,None,None]]

bf = [[None,None,None],
      [None,None,None],
      [None,None,None]]

rf = [[None,None,None],
      [None,None,None],
      [None,None,None]]

yf = [[None,None,None],
      [None,None,None],
      [None,None,None]]

state = [wf,gf,of,bf,rf,yf] # state is a cube. list of 2d lists(faces)
completeActionSequence = []
takeInput()
beginCFOP(state)
lengthOfCompleteActionSequence =calculateLengthoOfCompleteActionSequence(
                completeActionSequence)
print(lengthOfCompleteActionSequence)