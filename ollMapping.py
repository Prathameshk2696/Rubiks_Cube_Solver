# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 17:10:02 2020

@author: Prthamesh
"""

umcd = {0:"",1:"U1",2:"U2",3:"U'"} # u movement count dictionary

d = {
     # All edges flipped correctly
     "yynyyyny,nnynnnnnnynn":"R1U1R'U1R1U'R'U1R1U'R'U1R1U2R'", # Triple-Sune
     "yynynyny,nnnynnynnynn":"R'U'R1U'R'U2R1", # Antisune
     "nynynyny,ynynnnynynnn":"R1U1R'U1R1U'R'U1R1U2R'", # Double-Sune
     "nynyyyyy,nnnynnnnnnny":"r1U1R'U'r'F1r1F'", # Hammerhead
     "yynynyyy,nnnynynnnnnn":"R1U1R'U1R1U2R'R'U'R1U'R'U2R1", # Headlights
     "nynynyny,ynynnynnnynn":"R1U2R'R'U'R2U'R'R'U2R1", # Pi
     "nyyynyny,nnnnnynnynny":"R1U1R'U1R1U2R'", # Sune
     # No edges flipped correctly
     "nnnnnnnn,yyynynyyynyn":"R1U2R'R'F1R1F'U2R'F1R1F'", # Runway
     "nnnnnnnn,yyynyynynyyn":"F1R1U1R'U'F'f1R1U1R'U'f'", # Zamboni
     "nnnnynnn,nyynynnyynyy":"f1R1U1R'U'f'U'F1R1U1R'U'F'", # Anti-Mouse
     "nnnnnnyn,yynyynyynnyn":"f1R1U1R'U'f'U1F1R1U1R'U'F'", # mouse
     "ynnnynnn,nyynynnynyyn":"R1U1R'U'R'F1R1F'U2R'F1R1F'", # Slash
     "ynynnnnn,nynnynyyynyn":"F1R1U'R'U'R1U1R'F'U'F1R1U1R'U'F'", # Crown
     "ynnnnnyn,nyynynyynnyn":"M1U1R1U1R'U'M'R'F1R1F'", # Bunny
     # All corners oriented
     "yyynynyy,nnnnynnynnnn":"F1R1U1R'U'F'U2F1R1U1R'U'F'", # Fish
     "yyynyyyn,nnnnynnnnnyn":"R1U1R'U'M'U1R1U'r'", # H
     "ynynynyn,nynnynnynnyn":"M1U1R1U1R'U'M2U1R1U'r'", # X
     # Square shapes
     "nnnyyynn,nyynnnnnynyy":"r'U2R1U1R'U1r1", # Lefty square
     "nnnnnyyy,yynyynynnnnn":"r1U2R'U'R1U'r'", # Righty square
     # Big lightening bolt shapes
     "nyynnyyn,nnnnynynnnyy":"L1F'L'U'L1U1F1U'L'", # Fung
     "yynnyynn,nnynynnnnyyn":"R'F1R1U1R'U'F'U1R1", # Anti-fung
     # Small lightening bolt shapes
     "nyynnnny,nnnnyynyynny":"r1U1R'U1R1U2r'", # Lightening
     "nnnnyyny,yynyynnnnynn":"R1U2R'U2R'F1R1F'", # Reverse lightening
     "nynnnnyy,nnynyynynnny":"r1U1R'U1R'F1R1F'R1U2r'", # Downstairs
     "nnnynyyn,yynynnynnnyn":"F1R1U1R'U'F'U1F1R1U1R'U'F'", # Upstairs
     # Fish shapes
     "nynnynny,ynnyynnynynn":"R1U1R'U'R'F1R2U1R'U'F'", # kite
     "nynynnyn,nnynnynynnyy":"R1U1R'U'R'F1R1F'R1U1R'", # anti-kite
     "ynnyyynn,nynynnnnynyn":"R1U2R'R'F1R1F'R1U2R'", # Fish salad
     "yynnynny,nnnyynnyynnn":"F1R1U'R'U'R1U1R'F'", # Mounted fish
     # Knight move shapes
     "nyynnynn,nnnnyynnynyy":"r1U'r'U'r1U1r'y'R'U1R1", # Gun
     "nynnyynn,ynnyynnnnyyn":"l'U1l1U1l'U'l1y'R1U'R'", # Anti-gun
     "":"", # Squeegee
     "":"", # Anti-Squeegee
     }

def permute(s1,s2):
    temps1 = s1[2:]+s1[:2]
    temps2 = s2[3:]+s2[:3]
    return temps1,temps2    

def makeListOfActionSequence(actionSequence):
    l = []
    while actionSequence:
        l.append(actionSequence[0:2])
        actionSequence = actionSequence[2:]
    return l

def getSequence(caseKey):
    s1,s2 = caseKey.split(',')
    actionSequence = None
    for uMovementCount in range(4):
        if caseKey in d:
            actionSequence = umcd[uMovementCount] + d[caseKey]
        s1,s2 = permute(s1,s2)
        caseKey = s1+","+s2
    actionSequence = makeListOfActionSequence(actionSequence)
    return actionSequence
            