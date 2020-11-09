# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:15:01 2020

@author: Prthamesh
"""
from f2lGoals import (checkFrontRightInsertedPair,
                      checkFrontLeftInsertedPair,
                      checkBackRightInsertedPair,
                      checkBackLeftInsertedPair)

numberOfAllowedMoves = {}
reverseMoveDictionary = {"R":"R'","L":"L'","U":"U'","D":"D'","F":"F'","B":"B'",
                         "R'":"R","L'":"L","U'":"U","D'":"D","F'":"F","B'":"B"}

def initializeNumberOfAllowedMoves():
    for key in reverseMoveDictionary:
        numberOfAllowedMoves[key] = 1

def setNumberOfAllowedMoves(prev1):
    if prev1 not in numberOfAllowedMoves: return
    numberOfAllowedMoves[prev1] -= 1
    reverseMove = reverseMoveDictionary[prev1]
    numberOfAllowedMoves[reverseMove] += 1

def getAvailableActions(prev1,prev2,state):
    wf,gf,of,bf,rf,yf = state
    availableActions = ["R1","R'",
           "U1","U'","U2",
           "F1","F'",
           "L1","L'",
           "B1","B'",
           ]
    if checkFrontRightInsertedPair(state):
        l = ["R1","R2","F'","F2"]
        availableActions = [action for action in availableActions if action not in l]
    if checkFrontLeftInsertedPair(state):
        l = ["F1","F2","L'","L2"]
        availableActions = [action for action in availableActions if action not in l]
    if checkBackRightInsertedPair(state):
        l = ["R'","R2","B1","B2"]
        availableActions = [action for action in availableActions if action not in l]   
    if checkBackLeftInsertedPair(state):
        l = ["L1","L2","B'","B2"]
        availableActions = [action for action in availableActions if action not in l]
    
    if prev1!="U1" and prev1!="U2" and prev1!="U'":
        setNumberOfAllowedMoves(prev1)
    availableActions = [action for action in availableActions if action[0] != prev1[0]]
    return availableActions
