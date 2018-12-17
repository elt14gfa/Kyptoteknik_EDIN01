import numpy as np



def lfsr1(initState, z_seq):

    currentState = initState

    outputList = []

    for i in range(0, len(z_seq)):
        D0 = currentState[0]
        D1 = currentState[1]
        D2 = currentState[2]
        D4 = currentState[4]
        D6 = currentState[6]
        D7 = currentState[7]
        D10 = currentState[10]
        D11 = currentState[11]

        currentState = currentState[1:]
        currentState.append((D0 + D1 + D2 + D4 + D6 + D7 + D10 + D11) % 2)

        outputList.append(D0)

    return outputList

def keyGenerator(z_seq):
    dH = 0
    maxP = 0
    initState1 = [0,0,0,0,0,0,0,0,0,0,0,1]
    initState2 = np.zeros(15)
    initState3 = np.zeros(17)


    for i in range(0,2**len(initState1)):

        u1 = lfsr1(initState1,z_seq)
        print('u1', u1)
        for u,z in zip(u1,z_seq):
            if u != z:
                dH += 1

        tmpP = 1 - dH/len(z_seq)

        if maxP < tmpP:
            maxP = tmpP

        initState1 = u1[:13]

    return maxP

if __name__ == '__main__':

    z_seq = open("z_seq.txt", "r")
    z_seq = z_seq.read()

    print(z_seq)

    maxP = keyGenerator(z_seq)
    print(maxP)