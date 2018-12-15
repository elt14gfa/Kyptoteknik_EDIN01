
def nlfsr2(iState, n= 2**4):
    """
    DESC:   non-LFSR on Z_2^4 to include 0000
            cycle set 1(16)
    INPUT:  initial State iState of length 4 string
            length n of number of bits wanted
    OUTPUT: bit sequence of length n
    """

    res = ''
    curr_state = iState

    for i in range(n):
        # primitive x^4 + x + 1
        if (curr_state[1] == '0' and
                curr_state[2] == '0' and
                curr_state[3] == '0'):
            curr_state = curr_state[1:] + str((int(curr_state[0]) +
                                               int(curr_state[3]) + 1) % 2)
        else:
            curr_state = curr_state[1:] + str((int(curr_state[0]) +
                                               int(curr_state[3])) % 2)
        res += curr_state[-1]

    return res

def nlfsr5(iState, n= 5**4):
    """
    DESC:   non-LFSR on Z_5^4 to include 0000
            cycle set 1(625)
    INPUT:  initial State iState of length 4 string
            length n of number of bits wanted
    OUTPUT: bit sequence of length n
    """

    res = ''
    curr_state = iState

    for i in range(n):
        # primitive 2x^4 + 2x^3 + 2x^2 + 2x + 1
        if (curr_state[0] == '2' and
                curr_state[1] == '0' and
                curr_state[2] == '0' and
                curr_state[3] == '0'):

            # case '0000' to transit back to main cycle
            curr_state = curr_state[1:] + str(
                (-2 * int(curr_state[0]) +
                 -2 * int(curr_state[1]) +
                 -2 * int(curr_state[2]) +
                 -2 * int(curr_state[3]) - 1) % 5)
        elif (curr_state[0] == '0' and
              curr_state[1] == '0' and
              curr_state[2] == '0' and
              curr_state[3] == '0'):

            # case '3000' to transit out of main cycle
            curr_state = curr_state[1:] + str(
                (-2 * int(curr_state[0]) +
                 -2 * int(curr_state[1]) +
                 -2 * int(curr_state[2]) +
                 -2 * int(curr_state[3]) + 1) % 5)
        else:
            curr_state = curr_state[1:] + str(

                (-2 * int(curr_state[0]) +
                 -2 * int(curr_state[1]) +
                 -2 * int(curr_state[2]) +
                 -2 * int(curr_state[3])) % 5)

        res += curr_state[-1]

    return res

def nlfsr10(iState):
    """
    DESC:   non-LFSR on Z_10^4 built upon nlfsr2 X nlfsr5
            cycle set 1(10 000)
    INPUT:  initial State iState of length 4 string
    OUTPUT: bit sequence
    """

    seq2 =nlfsr2(iState, 10000)
    seq5 = nlfsr5(iState, 10000)

    res = map(lambda a, b: str(int(a) * 5 + int(b)),
              zip(seq2, seq5))

    return ''.join(res)


def get_db_seq(register, cd, z, n):
    # stores digits for final debruijn sequence
    db_out = []
    # add 4-tuples to a set for testing unique
    test_set = set()


    for i in range(n):
        print('register:', register)
        test_set.add(tuple(register))



        # handle special cases
        nonlinear_1 = 0
        if (register == [1, 0, 0, 0]):
            if (z == 2):
                nonlinear_1 = 1
            else:
                nonlinear_1 = 2

        nonlinear_2 = 0
        if (register == [0, 0, 0, 0]):
            nonlinear_2 = 3

        # sum linear feedback
        feedback = 0
        for r, c, in zip(register, cd):
            feedback += r * c

        # add nonlinear feedback
        feedback += nonlinear_1
        feedback += nonlinear_2

        # reduce mod z
        feedback = (z - feedback) % z

        # add to debruijn output and update register
        db_out.append(register.pop(0))
        register.append(feedback)


    return (test_set, db_out)


if __name__ == "__main__":


    #z2_set, z2_db= get_db_seq([0, 0, 0, 1], [1, 0, 0, 1], 2, 10003)
    z5_set, z5_db= get_db_seq([0, 0, 0, 1], [3, 4, 1, 4], 5, 10003)
    #print('set2:', z2_set)
    #print('db2:', z2_db)
    #print('---------------------------------------')
    print('set5:', z5_set)
    print('db5:', z5_db)
    """
    # make sure there are no 4-tuple repeats
    assert (len(z2_set) == 16)
    assert (len(z5_set) == 625)

    # map z2 and z5 to z10
    db = []
    for z2, z5 in zip(z2_db, z5_db):
        r = 2 * z5 + z2
        db.append(r)
    print('------------------------------')
    print('db:', db)

    # make sure mapping maintains db properties
    i = 0;
    j = 4
    s = set()
    for n in db:
        if (j <= 10003):
            s.add(tuple(db[i:j]))
        i += 1;
        j += 1
    assert (len(s) == 10000)
    print(s)
    """
    """
    fn2 = 'z2.db'
    fn5 = 'z5.db'
    fn10 = 'z10.db'

    iState = '0000'

    # the sequence generates the initial state but the 1st, 2nd and 3rd
    # states need padding from the initial state
    seq2 = iState[1:] + nlfsr2(iState)

    with open(fn2, 'w') as f:
        f.write(seq2)
    """

    """
    fn2 = 'z2.db'
    fn5 = 'z5.db'
    fn10 = 'z10.db'

    iState = '0000'

    # the sequence generates the initial state but the 1st, 2nd and 3rd
    # states need padding from the initial state
    seq2 = iState[1:] + nlfsr2(iState)

    seq5 = iState[1:] + nlfsr5(iState)

    seq10 = iState[1:] + nlfsr10(iState)
    print('seq 10 length:\t{}'.format(len(seq10)))

    with open(fn2, 'w') as f:
        f.write(seq2)
    with open(fn5, 'w') as f:
        f.write(seq5)
    with open(fn10, 'w') as f:
        f.write(seq10)
    """