import numpy as np
import pickle
import re
import string



def dB_z2 (initState = [0,0,0,1], iterations = 10003, feedback = [1,0,0,1]):
    currentState = initState
    specialState1 = [1,0,0,0]
    specialState2 = [0,0,0,0]
    deBruijn_z2 = []
    stateList = []

    #x^4 + x^3 + 1

    for iter in range(0,iterations):

        if currentState not in stateList:
            stateList.append(currentState)

        if np.array_equal(currentState, specialState1):
            c0 = currentState[0]
            currentState = [0,0,0,0]

        elif np.array_equal(currentState, specialState2):
            c0 = currentState[0]
            currentState = [0,0,0,1]

        else:
            c0 = currentState[0]
            c3 = currentState[3]
            currentState = currentState[1:]
            currentState.append((c0 + c3) % 2)


        deBruijn_z2.append(c0)

    return deBruijn_z2, stateList

def dB_z5 (initState = [0,0,0,0], iterations = 10003):
    currentState = initState
    specialState1 = [2,0,0,0]
    specialState2 = [0,0,0,0]
    deBruijn_z5 = []
    stateList = []

    #equation x^4+x^2+2x+2

    polyC0 = 3  #-2 mod 5
    polyC1 = 3  #-2 mod 5
    polyC2 = 4  #-1 mod 5

    for iter in range(0,iterations):

        if currentState not in stateList:
            stateList.append(currentState)

        if np.array_equal(currentState, specialState1):
            c0 = currentState[0]
            currentState = [0,0,0,0]

        elif np.array_equal(currentState, specialState2):
            c0 = currentState[0]
            currentState = [0,0,0,1]

        else:
            c0 = currentState[0]
            c1 = currentState[1]
            c2 = currentState[2]
            c3 = currentState[3]
            currentState = currentState[1:]
            currentState.append((polyC0*c0 + polyC1*c1 + polyC2*c2) % 5)


        deBruijn_z5.append(c0)

    return deBruijn_z5, stateList



def db_z10(dbSeq_z2,dbSeq_z5):
    deBruijn_z10 = []

    for z2, z5 in zip(dbSeq_z2,dbSeq_z5):
        deBruijn_z10.append(z2 + z5*2)

    return deBruijn_z10

if __name__ == '__main__':
    deBruin_z2, stateList1 = dB_z2()
    print('Z2')
    print(deBruin_z2)

    print(stateList1,'\n')
    print('lenStateList1z2:', len(stateList1))
    print('lenDeBruijnz2:', len(deBruin_z2), '\n')
    print('------------')

    deBruijn_z5, stateList2 = dB_z5()
    print('Z5')
    print(deBruijn_z5)

    print(stateList2, '\n')
    print('stateList2z5:', len(stateList2))
    print('lenDeBruijnz5:', len(deBruijn_z5), '\n')
    print(stateList2[-1])
    print('------------')

    deBruijn_z10 = db_z10(deBruin_z2,deBruijn_z5)
    print('Z10')
    print(deBruijn_z10)
    print('lenDeBruijnz10:', len(deBruijn_z10))

    stringSeq = ''
    for i in deBruijn_z10:
        element = str(i)
        stringSeq += element
    with open('stringSeq', 'w') as f:
        f.write(stringSeq)

    listChecker = []

    for i in range(0,10000):
        current = [deBruijn_z10[i], deBruijn_z10[i+1], deBruijn_z10[i+2], deBruijn_z10[i+3]]
        if current not in listChecker:
            print('not in listCHecker:', current)
            listChecker.append(current)
        else:
            print('already in clistchecker:', current)