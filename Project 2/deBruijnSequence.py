import numpy as np




def dB_z2 (initState = [0,0,0,1], iterations = 10003, feedback = [1,0,0,1]):
    currentState = initState
    specialState1 = [1,0,0,0]
    specialState2 = [0,0,0,0]
    deBruijn_z2 = []
    stateList = []

    #x^4 + x^3 + 1

    for iter in range(1,iterations):

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
    specialState1 = [1,0,0,0]
    specialState2 = [0,0,0,0]
    deBruijn_z2 = []
    stateList = []

    polyC0 = 1
    polyC1 = 2
    polyC2 = 2


    #x^4 + x^3 + 1

    for iter in range(1,iterations):

        if currentState not in stateList:
            stateList.append(currentState)
        """
        if np.array_equal(currentState, specialState1):
            c0 = currentState[0]
            currentState = [0,0,0,0]
        """
        if np.array_equal(currentState, specialState2):
            c0 = currentState[0]
            currentState = [0,0,0,1]

        else:
            c0 = currentState[0]
            c1 = currentState[1]
            c2 = currentState[2]
            c3 = currentState[3]
            currentState = currentState[1:]
            currentState.append((c0 + 1*c1 + 2*c2 + c3*2) % 5)


        deBruijn_z2.append(c0)

    return deBruijn_z2, stateList


if __name__ == '__main__':
    deBruin_z2, stateList1 = dB_z2()
    print('Z2')
    print(deBruin_z2)
    print('------------')
    print(stateList1,'\n')

    deBruin_z5, stateList2 = dB_z5()
    print('Z5')
    print(deBruin_z5)
    print('------------')
    print(stateList2)
    print(len(stateList2))
