#!/usr/bin/env python

import random

def Splitter(A, S=[], skip=0, taken_and_returned=[]):
    """
    inputs: A is a list of positive integers
    return: 2 lists such that they sum up to the same number, or, False
    A: The lower order list
    S: The Higher order list
    """
    if (S == []) and (sum(A)%2 != 0):
        return "No solution possible because sum of A is an Odd number"
    if sum(S) == sum(A):
        return A, S, skip, taken_and_returned, sum(A), sum(S)
    elif sum(S) <= sum(A):
        # print("##", A, S)
        # find the highest element in A such that when appened to S, sum(S) is still < sum(A) - element
        if sum(S) + sorted(A)[0] > sum(sorted(A)[1:]):
            skip = skip + 1
            if skip == len(A) + len(S):
                return "No more skips left. No solution possible"
            min_S = min(S)
            S.pop(S.index(min_S))
            A.append(min_S)
            print("Return", min_S, "to A; ", "; SumA is ", sum(A), "; SumS is", sum(S))
            taken_and_returned.append(min_S)
            return Splitter(A, S, skip, taken_and_returned)
        else:
            for i in reversed(sorted(A)[0:len(A)-skip]):
                if sum(S) + i <= sum(A) - i:
                    # if i in taken_and_returned:
                    #     return "avoiding pointless Loop. No solution possible"
                    S.append(i)
                    A.pop(A.index(i))
                    print("Take", i, "from A and move it to S", ";SumA is ", sum(A), "; SumS is", sum(S))
                    return Splitter(A, S, skip, taken_and_returned)
            return "Loop done. No solution possible"
    else:
        return "No solution possible"



def main():

    # A = [1,3, 4, 6, 2]
    # A = [11,9,15,16, 8, 3, 2]
    A = list(range(1,204,4))
    random.shuffle(A)
    print("Sum of A is:", sum(A), "and A is ", A)
    RES = Splitter(A, [])
    print(RES)


if __name__ == '__main__':
    main()