""" function to display board
Inputs:
1)outPutVar1(P1)
2)outPutVar2(P2)
3)outPutVar3(P3)
4)outPutVar4(Q1)
5)outPutVar5(Q2)
6)outPutVar6(Q3)
7)outPutVar7(R1)
8)outPutVar8(R2)
9)outPutVar9(R3)

Output:
3 x 3 tiled board which contains the coordinates
"""
def displayBoard(outPutVar1, outPutVar2, outPutVar3,
                 outPutVar4, outPutVar5, outPutVar6,
                 outPutVar7, outPutVar8, outPutVar9):
    
    print "\n"
    print "Board"
    print "-----------------"
    print outPutVar1+"\t", outPutVar2+"\t",outPutVar3+"\n"
    print outPutVar4+"\t", outPutVar5+"\t",outPutVar6+"\n"
    print outPutVar7+"\t", outPutVar8+"\t",outPutVar9
    print "\n"+"\n"

""" function to check input for P1
Inputs:
1)varInput(the value of P1)

Output:
returns the value of varInput
"""
def checkInputForP1(varInput):
    return varInput

""" function to check input for P2
Inputs:
1)varInput(the value of P2)
2)varP1(the value of P1)

Output:
returns the value of varInput if varInput compared with varP1 are not same
returns "False" if both values of varInput compared with varP1 are the same
"""
def checkInputForP2(varInput, varP1):
    if(varInput == varP1):
        return "False"
    else:
        return varInput

""" function to check input for P3
Inputs:
1)varInput(the value of P3)
2)varP1(the value of P1)
2)varP2(the value of P2)

Output:
returns the value of varInput if varInput compared with varP1 and varP2 are not same
returns "False" if both values of varInput compared with varP1 and varP2 are the same
"""
def checkInputForP3(varInput, varP1, varP2):
    if(varInput == varP1 or varInput == varP2):
        return "False"
    else:
        return varInput

""" function to check input for Q1
Inputs:
1)varInput(the value of Q1)
2)varP1(the value of P1)
2)varP2(the value of P2)

Output:
returns the value of varInput if varInput compared with varP1 and varP2 are not same
returns "False" if both values of varInput compared with varP1 and varP2 are the same
"""
def checkInputForQ1(varInput, varP1, varP2):
    if(varInput == varP1 or varInput == varP2):
        return "False"
    else:
        return varInput

""" function to check input for Q2
Inputs:
1)varInput(the value of Q2)
2)varQ1(the value of Q1)
2)varP2(the value of P2)

Output:
returns the value of varInput if varInput compared with varQ1 and varP2 are not same
returns "False" if both values of varInput compared with varQ1 and varP2 are the same
"""
def checkInputForQ2(varInput, varP2, varQ1):
    if(varInput == varP2 or varInput == varQ1):
        return "False"
    else:
        return varInput

""" function to check input for Q3
Inputs:
1)varInput(the value of Q3)
2)varQ1(the value of Q1)
3)varQ2(the value of Q2)
4)varP3(the value of P3)

Output:
returns the value of varInput if varInput compared with varQ1, varQ2 and varP3 are not same
returns "False" if both values of varInput compared with varQ1, varQ2 and varP3 are the same
"""
def checkInputForQ3(varInput, varP3, varQ1, varQ2):
    if(varInput == varP3 or varInput == varQ1 or varInput == varQ2):
        return "False"
    else:
        return varInput

""" function to check input for R1
Inputs:
1)varInput(the value of R1)
2)varQ1(the value of Q1)
3)varP1(the value of P1)

Output:
returns the value of varInput if varInput compared with varQ1 and varP1 are not same
returns "False" if both values of varInput compared with varQ1 and varP1 are the same
"""
def checkInputForR1(varInput, varQ1, varP1):
    if(varInput == varQ1 or varInput == varP1):
        return "False"
    else:
        return varInput

""" function to check input for R2
Inputs:
1)varInput(the value of R2)
2)varR1(the value of R1)
3)varQ2(the value of Q2)
4)varP2(the value of P2)

Output:
returns the value of varInput if varInput compared with varR1, varQ2 and varP2 are not same
returns "False" if both values of varInput compared with varR1, varQ2 and varP2 are the same
"""
def checkInputForR2(varInput, varR1, varQ2, varP2):
    if(varInput == varR1 or varInput == varQ2 or varInput == varP2):
        return "False"
    else:
        return varInput

""" function to check input for R3
Inputs:
1)varInput(the value of R3)
2)varR1(the value of R1)
2)varR2(the value of R2)
2)varQ3(the value of Q3)
3)varP3(the value of P3)

Output:
returns the value of varInput if varInput compared with varR1, varR2, varQ3 and varP3 are not same
returns "False" if both values of varInput compared with varR1, varR2, varQ3 and varP3 are the same
"""
def checkInputForR3(varInput, varR1, varR2, varQ3, varP3):
    if(varInput == varR1 or varInput == varR2 or varInput == varQ3 or varInput == varP3):
        return "False"
    else:
        return varInput

""" function to validate input of any coordinate
Inputs:
1)varInput(the value of any coodinate)

Output:
returns False if varInput not strictly A or B or C
returns True if varInput is either A, B or C
"""
def validateInput(varInput):
    if(not varInput == "A" and not varInput == "B" and not varInput == "C"):
        return False
    else:
        return True

""" function to display invalid message
Output:
prints "invalid input"
"""
def displayInvalidMessage():
    print "invalid input"
