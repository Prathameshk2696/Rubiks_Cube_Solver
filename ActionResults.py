# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 23:53:37 2020

@author: Prthamesh
"""
import copy
# 1 clockwise rotation of complete face
def rotate(face):
    col1 = [row[0] for row in face]
    col2 = [row[1] for row in face]
    col3 = [row[2] for row in face]
    col1.reverse() ; col2.reverse() ; col3.reverse()
    face = [col1,col2,col3]
    return face

def displayState(state):
    for face in state:
        for row in face:
            print(row)
        print()

def rightAction(state,count):
    wf,gf,of,bf,rf,yf = state
    wf2 = copy.deepcopy(wf)
    gf2 = copy.deepcopy(gf)
    bf2 = copy.deepcopy(bf)
    yf2 = copy.deepcopy(yf)
    for i in range(count):
        for row in range(3):
            gf2[row][2] = wf[row][2]
            yf2[row][2] = gf[row][2]
            bf2[2-row][0] = yf[row][2]
            wf2[row][2] = bf[2-row][0]
        wf = copy.deepcopy(wf2)
        gf = copy.deepcopy(gf2)
        bf = copy.deepcopy(bf2)
        yf = copy.deepcopy(yf2)
        of = rotate(of)
    state = [wf,gf,of,bf,rf,yf]
    return state

def leftAction(state,count):
    wf,gf,of,bf,rf,yf = state
    wf2 = copy.deepcopy(wf)
    gf2 = copy.deepcopy(gf)
    bf2 = copy.deepcopy(bf)
    yf2 = copy.deepcopy(yf)
    for i in range(count):
        for row in range(3):
            gf2[row][0] = yf[row][0]
            yf2[row][0] = bf[2-row][2]
            bf2[2-row][2] = wf[row][0]
            wf2[row][0] = gf[row][0]
        wf = copy.deepcopy(wf2)
        gf = copy.deepcopy(gf2)
        bf = copy.deepcopy(bf2)
        yf = copy.deepcopy(yf2)
        rf = rotate(rf)
    state = [wf,gf,of,bf,rf,yf]
    return state

def upAction(state,count):
    wf,gf,of,bf,rf,yf = state
    gf2 = copy.deepcopy(gf)
    of2 = copy.deepcopy(of)
    bf2 = copy.deepcopy(bf)
    rf2 = copy.deepcopy(rf)
    for i in range(count):
        for col in range(3):
            gf2[0][col] = of[0][col]
            of2[0][col] = bf[0][col]
            bf2[0][col] = rf[0][col]
            rf2[0][col] = gf[0][col]
        gf = copy.deepcopy(gf2)
        of = copy.deepcopy(of2)
        bf = copy.deepcopy(bf2)
        rf = copy.deepcopy(rf2)
        yf = rotate(yf)
    state = [wf,gf,of,bf,rf,yf]
    return state

def downAction(state,count):
    wf,gf,of,bf,rf,yf = state
    gf2 = copy.deepcopy(gf)
    of2 = copy.deepcopy(of)
    bf2 = copy.deepcopy(bf)
    rf2 = copy.deepcopy(rf)
    for i in range(count):
        for col in range(3):
            gf2[2][col] = rf[2][col]
            rf2[2][col] = bf[2][col]
            bf2[2][col] = of[2][col]
            of2[2][col] = gf[2][col]
        gf = copy.deepcopy(gf2)
        of = copy.deepcopy(of2)
        bf = copy.deepcopy(bf2)
        rf = copy.deepcopy(rf2)
        wf = rotate(wf)
    state = [wf,gf,of,bf,rf,yf]
    return state

def frontAction(state,count):
    wf,gf,of,bf,rf,yf = state
    yf2 = copy.deepcopy(yf)
    of2 = copy.deepcopy(of)
    wf2 = copy.deepcopy(wf)
    rf2 = copy.deepcopy(rf)
    for i in range(count):
        for row in range(3):
            of2[row][0] = yf[2][row]
            wf2[0][2-row] = of[row][0]
            rf2[2-row][2] = wf[0][2-row]
            yf2[2][row] = rf[2-row][2]
        of = copy.deepcopy(of2)
        wf = copy.deepcopy(wf2)
        rf = copy.deepcopy(rf2)
        yf = copy.deepcopy(yf2)
        gf = rotate(gf)
    state = [wf,gf,of,bf,rf,yf]
    return state

def backAction(state,count):
    wf,gf,of,bf,rf,yf = state
    yf2 = copy.deepcopy(yf)
    of2 = copy.deepcopy(of)
    wf2 = copy.deepcopy(wf)
    rf2 = copy.deepcopy(rf)
    for i in range(count):
        for row in range(3):
            yf2[0][row] = of[row][2]
            rf2[2-row][0] = yf[0][row]
            wf2[2][2-row] = rf[2-row][0]
            of2[row][2] = wf[2][2-row]
        yf = copy.deepcopy(yf2)
        rf = copy.deepcopy(rf2)
        wf = copy.deepcopy(wf2)
        of = copy.deepcopy(of2)
        bf = rotate(bf)
    state = [wf,gf,of,bf,rf,yf]
    return state