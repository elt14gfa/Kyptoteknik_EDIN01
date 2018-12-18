import numpy as np



def lfsr1(initState, z_seq):

    currentState = initState

    outputList = ''

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
        currentState += str((int(D0) + int(D1) + int(D2) + int(D4) + int(D6) + int(D7) + int(D10) + int(D11)) % 2)
        outputList += D0
    return outputList

def keyGenerator(z_seq):

    maxP = 0
    initState1 = '0000000000001'
    initState2 = np.zeros(15)
    initState3 = np.zeros(17)
    de_bruijn = ''
    #listChecker = []

    currentState1 = initState1
    for i in range(0,2**len(currentState1)+12):

        if currentState1 == '1000000000000':
            D0 = currentState1[0]
            currentState1 = '0000000000000'
        else:
            D0 = currentState1[0]
            D1 = currentState1[1]
            D2 = currentState1[2]
            D4 = currentState1[4]
            D6 = currentState1[6]
            D7 = currentState1[7]
            D10 = currentState1[10]
            D11 = currentState1[11]
            currentState1 = currentState1[1:]
            currentState1 += str((int(D0) + int(D1) + int(D2) + int(D4) + int(D6) + int(D7) + int(D10) + int(D11)) % 2)
        de_bruijn += D0
    #print((de_bruijn))
    for i in range(0,2**len(initState1)):

        dH = 0
        u1 = lfsr1(initState1,z_seq)

        u1 = str(u1)

        for u,z in zip(u1,z_seq):
            if u is not z:
                dH += 1
        #print('state:', initState1, 'dH: ', dH)

        tmpP = 1 - dH/len(z_seq)

        if maxP < tmpP:
            optimalState = initState1
            optimalU1 = u1
            maxP = tmpP
        if initState1 == '0110011000011':
            print(initState1, tmpP)
        initState1 = de_bruijn[i+1:i+14]

        #if de_bruijn[i+1:i+14] not in listChecker:
        #    listChecker.append(de_bruijn[i+1:i+14])
        #else:
        #    print('duplet:', de_bruijn[i+1:i+14])

    return maxP, optimalState , optimalU1

if __name__ == '__main__':

    z_seq = open("z_seq.txt", "r")
    z_seq = z_seq.read()

    print(len(z_seq))

    maxP, optimalState, optimalU1 = keyGenerator(z_seq)
    print(maxP)
    print(optimalState)
    print(optimalU1)
    print(z_seq)