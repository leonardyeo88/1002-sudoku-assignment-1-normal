import functions

varP1 = "P1"        #init coordinate P1                                                     
varP2 = "P2"        #init coordinate P2
varP3 = "P3"        #init coordinate P3

varQ1 = "Q1"        #init coordinate Q1
varQ2 = "Q2"        #init coordinate Q2
varQ3 = "Q3"        #init coordinate Q3

varR1 = "R1"        #init coordinate R1
varR2 = "R2"        #init coordinate R2
varR3 = "R3"        #init coordinate R3

''' --- start main --- '''
functions.displayBoard(varP1, varP2, varP3, #display empty board
                       varQ1, varQ2, varQ3,
                       varR1, varR2, varR3) 

""" ---coordinate P1 start--- """

continueVar = "False"                                           #init counter variable as "False"

while(continueVar == "False"):                                  #loops infinitely until counter variable changes to "True"
    varP1 = raw_input("Enter P1: ")                             #user input for P1
    varP1 = varP1.upper()                                       #value for P1 converts to uppercase
    if(not functions.validateInput(varP1)):                     #checks if input for P1 is invalid(must be A, B and C. No other values or empty value)
        functions.displayInvalidMessage()                       #display message if invalid input
        continueVar = "False"                                   #counter variable changes to "False"
    else:                                                       #if input for P1 is valid
        getInputP1 = functions.checkInputForP1(varP1)           #checks if P1 could be placed on the board
        if(getInputP1):                                         #if P1 could be placed on the board, 
            functions.displayBoard(getInputP1,varP2, varP3,     #display board with P1 included
                 varQ1, varQ2, varQ3,
                 varR1, varR2, varR3)
            continueVar = "True"                                #counter variable changes to "True"

""" ---coordinate P1 end--- """

""" ---coordinate P2 start--- """

continueVar = "False"                                                   #init counter variable as "False"

while(continueVar == "False"):                                          #loops infinitely until counter variable changes to "True"
    varP2 = raw_input("Enter P2: ")                                     #user input for P2
    varP2 = varP2.upper()                                               #value for P2 converts to uppercase
    if(not functions.validateInput(varP2)):                             #checks if input for P2 is invalid(must be A, B and C. No other values or empty value)
        functions.displayInvalidMessage()                               #display message if invalid input
        continueVar = "False"                                           #counter variable changes to "False"
    else:                                                               #if input for P2 is valid
        getInputP2 = functions.checkInputForP2(varP2, getInputP1)       #checks if P2 could be placed on the board
        if(getInputP2 != "False"):                                      #if P2 could be placed on the board, 
            functions.displayBoard(getInputP1,getInputP2, varP3,        #display board with P2 included
                 varQ1, varQ2, varQ3,
                 varR1, varR2, varR3)
            continueVar = "True"                                        #counter variable changes to "True"
        else:
            functions.displayInvalidMessage()                           #display message if invalid input
            continueVar = "False"                                       #counter variable changes to "False"

""" ---coordinate P2 end--- """

""" ---coordinate P3 start--- """

continueVar = "False"                                                           #init counter variable as "False"

while(continueVar == "False"):                                                  #loops infinitely until counter variable changes to "True"
    varP3 = raw_input("Enter P3: ")                                             #user input for P3
    varP3 = varP3.upper()                                                       #value for P3 converts to uppercase        
    if(not functions.validateInput(varP3)):                                     #checks if input for P3 is invalid(must be A, B and C. No other values or empty value)
        functions.displayInvalidMessage()                                       #display message if invalid input
        continueVar = "False"                                                   #counter variable changes to "False"
    else:                                                                       #if input for P3 is valid
        getInputP3 = functions.checkInputForP3(varP3, getInputP1, getInputP2)   #checks if P3 could be placed on the board
        if(getInputP3 != "False"):                                              #if P3 could be placed on the board,
            functions.displayBoard(getInputP1,getInputP2, getInputP3,           #display board with P3 included
                 varQ1, varQ2, varQ3,
                 varR1, varR2, varR3)
            continueVar = "True"                                                #counter variable changes to "True"
        else:
            functions.displayInvalidMessage()                                   #display message if invalid input
            continueVar = "False"                                               #counter variable changes to "False"

""" ---coordinate P3 end--- """

""" ---coordinate Q1 start--- """

continueVar = "False"                                                               #init counter variable as "False"

while(continueVar == "False"):                                                      #loops infinitely until counter variable changes to "True"
    varQ1 = raw_input("Enter Q1: ")                                                 #user input for Q1
    varQ1 = varQ1.upper()                                                           #value for Q1 converts to uppercase
    if(not functions.validateInput(varQ1)):                                         #checks if input for Q1 is invalid(must be A, B and C. No other values or empty value)
        functions.displayInvalidMessage()                                           #display message if invalid input
        continueVar = "False"                                                       #counter variable changes to "False"
    else:                                                                           #if input for Q1 is valid
        getInputQ1 = functions.checkInputForQ1(varQ1, getInputP1, getInputP2)       #checks if Q1 could be placed on the board
        if(getInputQ1 != "False"):                                                  #if Q1 could be placed on the board,
            functions.displayBoard(getInputP1,getInputP2, getInputP3,               #display board with Q1 included
                 getInputQ1, varQ2, varQ3,
                 varR1, varR2, varR3)
            continueVar = "True"                                                    #counter variable changes to "True"
        else:
            functions.displayInvalidMessage()                                       #display message if invalid input
            continueVar = "False"                                                   #counter variable changes to "False"

""" ---coordinate Q1 end--- """

continueVar = "False"

while(continueVar == "False"):
    varQ2 = raw_input("Enter Q2: ")
    varQ2 = varQ2.upper()
    if(not functions.validateInput(varQ2)):
        functions.displayInvalidMessage()
        continueVar = "False"
    else:
        getInputQ2 = functions.checkInputForQ2(varQ2, getInputP2, getInputQ1)                           #
        if(getInputQ2 != "False"):
            functions.displayBoard(getInputP1,getInputP2, getInputP3,
                 getInputQ1, getInputQ2, var6,
                 var7, var8, var9)
            continueVar = "True"
        else:
            functions.displayInvalidMessage()
            continueVar = "False"


continueVar = "False"

while(continueVar == "False"):
    varQ3 = raw_input("Enter Q3: ")
    varQ3 = varQ3.upper()
    if(not functions.validateInput(varQ3)):
        functions.displayInvalidMessage()
        continueVar = "False"
    else:
        getInputQ3 = functions.checkInputForQ3(varQ3, getInputP3, getInputQ1, getInputQ2)               #
        if(getInputQ3 != "False"):
            functions.displayBoard(getInputP1,getInputP2, getInputP3,
                 getInputQ1, getInputQ2, getInputQ3,
                 var7, var8, var9)
            continueVar = "True"
        else:
            functions.displayInvalidMessage()
            continueVar = "False"


continueVar = "False"

while(continueVar == "False"):
    varR1 = raw_input("Enter R1: ")
    varR1 = varR1.upper()
    if(not functions.validateInput(varR1)):
        functions.displayInvalidMessage()
        continueVar = "False"
    else:
        getInputR1 = functions.checkInputForR1(varR1, getInputQ1, getInputP1)                           #
        if(getInputR1 != "False"):
            functions.displayBoard(getInputP1,getInputP2, getInputP3,
                 getInputQ1, getInputQ2, getInputQ3,
                 getInputR1, var8, var9)
            continueVar = "True"
        else:
            functions.displayInvalidMessage()
            continueVar = "False"


continueVar = "False"

while(continueVar == "False"):
    varR2 = raw_input("Enter R2: ")
    varR2 = varR2.upper()
    if(not functions.validateInput(varR2)):
        functions.displayInvalidMessage()
        continueVar = "False"
    else:
        getInputR2 = functions.checkInputForR2(varR2, getInputR1, getInputQ2, getInputP2)               #
        if(getInputR2 != "False"):
            functions.displayBoard(getInputP1,getInputP2, getInputP3,
                 getInputQ1, getInputQ2, getInputQ3,
                 getInputR1, getInputR2, var9)
            continueVar = "True"
        else:
            functions.displayInvalidMessage()
            continueVar = "False"


continueVar = "False"

while(continueVar == "False"):
    varR3 = raw_input("Enter R3: ")
    varR3 = varR3.upper()
    if(not functions.validateInput(varR3)):
        functions.displayInvalidMessage()
        continueVar = "False"
    else:
        getInputR3 = functions.checkInputForR3(varR3, getInputR1, getInputR2, getInputQ3, getInputP3)   #
        if(getInputR3 != "False"):
            functions.displayBoard(getInputP1,getInputP2, getInputP3,
                 getInputQ1, getInputQ2, getInputQ3,
                 getInputR1, getInputR2, getInputR3)
            continueVar = "True"
        else:
            functions.displayInvalidMessage()
            continueVar = "False"

print "Board generated"

''' --- end main --- '''
