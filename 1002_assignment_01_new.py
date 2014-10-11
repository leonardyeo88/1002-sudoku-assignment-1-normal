
var1 = "P1"
var2 = "P2"
var3 = "P3"

var4 = "Q1"
var5 = "Q2"
var6 = "Q3"

var7 = "R1"
var8 = "R2"
var9 = "R3"


def displayBoard(outPutVar1, outPutVar2, outPutVar3,
                 outPutVar4, outPutVar5, outPutVar6,
                 outPutVar7, outPutVar8, outPutVar9):
    
    print "Board"
    print "-----------------"
    print outPutVar1+"\t", outPutVar2+"\t",outPutVar3+"\n"
    print outPutVar4+"\t", outPutVar5+"\t",outPutVar6+"\n"
    print outPutVar7+"\t", outPutVar8+"\t",outPutVar9
    print "\n"+"\n"

def checkInputForP1(varInput):
    return varInput

def checkInputForP2(varInput, varP1):
    if(varInput == varP1):
        return "False"
    else:
        return varInput

def checkInputForP3(varInput, varP1, varP2):
    if(varInput == varP1 or varInput == varP2):
        return "False"
    else:
        return varInput

def checkInputForQ1(varInput, varP1, varP2):
    if(varInput == varP1 or varInput == varP2):
        return "False"
    else:
        return varInput

def checkInputForQ2(varInput, varP2, varQ1):
    if(varInput == varP2 or varInput == varQ1):
        return "False"
    else:
        return varInput

def checkInputForQ3(varInput, varP3, varQ1, varQ2):
    if(varInput == varP3 or varInput == varQ1 or varInput == varQ2):
        return "False"
    else:
        return varInput

def checkInputForR1(varInput, varQ1, varP1):
    if(varInput == varQ1 or varInput == varP1):
        return "False"
    else:
        return varInput

def checkInputForR2(varInput, varR1, varQ2, varP2):
    if(varInput == varR1 or varInput == varQ2 or varInput == varP2):
        return "False"
    else:
        return varInput

def checkInputForR3(varInput, varR1, varR2, varQ3, varP3):
    if(varInput == varR1 or varInput == varR2 or varInput == varQ3 or varInput == varP3):
        return "False"
    else:
        return varInput
    

''' --- start main --- '''
displayBoard(var1, var2, var3, var4, var5, var6, var7, var8, var9) #display empty board

continueVar = "False"

while(continueVar == "False"):
    varP1 = raw_input("Enter P1: ")
    getInputP1 = checkInputForP1(varP1.upper())
    if(getInputP1):
        displayBoard(getInputP1,var2, var3,
             var4, var5, var6,
             var7, var8, var9)
        continueVar = "True"


continueVar = "False"

while(continueVar == "False"):
    varP2 = raw_input("Enter P2: ")
    getInputP2 = checkInputForP2(varP2.upper(), getInputP1)
    if(getInputP2 != "False"):
        displayBoard(getInputP1,getInputP2, var3,
             var4, var5, var6,
             var7, var8, var9)
        continueVar = "True"
    else:
        print "invalid"
        continueVar = "False"


continueVar = "False"

while(continueVar == "False"):
    varP3 = raw_input("Enter P3: ")
    getInputP3 = checkInputForP3(varP3.upper(), getInputP1, getInputP2)
    if(getInputP3 != "False"):
        displayBoard(getInputP1,getInputP2, getInputP3,
             var4, var5, var6,
             var7, var8, var9)
        continueVar = "True"
    else:
        print "invalid"
        continueVar = "False"


continueVar = "False"

while(continueVar == "False"):
    varQ1 = raw_input("Enter Q1: ")
    getInputQ1 = checkInputForQ1(varQ1.upper(), getInputP1, getInputP2)
    if(getInputQ1 != "False"):
        displayBoard(getInputP1,getInputP2, getInputP3,
             getInputQ1, var5, var6,
             var7, var8, var9)
        continueVar = "True"
    else:
        print "invalid"
        continueVar = "False"


continueVar = "False"

while(continueVar == "False"):
    varQ2 = raw_input("Enter Q2: ")
    getInputQ2 = checkInputForQ2(varQ2.upper(), getInputP2, getInputQ1)
    if(getInputQ2 != "False"):
        displayBoard(getInputP1,getInputP2, getInputP3,
             getInputQ1, getInputQ2, var6,
             var7, var8, var9)
        continueVar = "True"
    else:
        print "invalid"
        continueVar = "False"


continueVar = "False"

while(continueVar == "False"):
    varQ3 = raw_input("Enter Q3: ")
    getInputQ3 = checkInputForQ3(varQ3.upper(), getInputP3, getInputQ1, getInputQ2)
    if(getInputQ3 != "False"):
        displayBoard(getInputP1,getInputP2, getInputP3,
             getInputQ1, getInputQ2, getInputQ3,
             var7, var8, var9)
        continueVar = "True"
    else:
        print "invalid"
        continueVar = "False"


continueVar = "False"

while(continueVar == "False"):
    varR1 = raw_input("Enter R1: ")
    getInputR1 = checkInputForR1(varR1.upper(), getInputQ1, getInputP1)
    if(getInputR1 != "False"):
        displayBoard(getInputP1,getInputP2, getInputP3,
             getInputQ1, getInputQ2, getInputQ3,
             getInputR1, var8, var9)
        continueVar = "True"
    else:
        print "invalid"
        continueVar = "False"


continueVar = "False"

while(continueVar == "False"):
    varR2 = raw_input("Enter R2: ")
    getInputR2 = checkInputForR2(varR2.upper(), getInputR1, getInputQ2, getInputP2)
    if(getInputR2 != "False"):
        displayBoard(getInputP1,getInputP2, getInputP3,
             getInputQ1, getInputQ2, getInputQ3,
             getInputR1, getInputR2, var9)
        continueVar = "True"
    else:
        print "invalid"
        continueVar = "False"


continueVar = "False"

while(continueVar == "False"):
    varR3 = raw_input("Enter R3: ")
    getInputR3 = checkInputForR3(varR3.upper(), getInputR1, getInputR2, getInputQ3, getInputP3)
    if(getInputR3 != "False"):
        displayBoard(getInputP1,getInputP2, getInputP3,
             getInputQ1, getInputQ2, getInputQ3,
             getInputR1, getInputR2, getInputR3)
        continueVar = "True"
    else:
        print "invalid"
        continueVar = "False"

print "Board generated"

''' --- end main --- '''
