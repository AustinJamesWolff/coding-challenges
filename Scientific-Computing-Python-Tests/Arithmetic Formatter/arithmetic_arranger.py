def arithmetic_arranger(problems, show = False):
    
    # These lists will store the values for each equation (index) in the problems list.
    twoDList = []
    dashes = []
    ReNum1 = []
    ReNum2 = []
    ReOp = []
    equaLen = []
    answers = []
    topNum = []
    bottomNum = []
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for i in range(len(problems)):
        twoDList.append(problems[i].split(" "))
        
        try: 
            int(twoDList[i][0])
            int(twoDList[i][2])
        except:
            return "Error: Numbers must only contain digits."
        
        ReNum1.append(int(twoDList[i][0]))
        if ReNum1[i] > 9999:
            return "Error: Numbers cannot be more than four digits."
            
        ReOp.append(twoDList[i][1])
        if ReOp[i] != '+' and ReOp[i] != '-':
            return "Error: Operator must be '+' or '-'."
            
        ReNum2.append(int(twoDList[i][2]))
        if ReNum2[i] > 9999:
            return "Error: Numbers cannot be more than four digits."
                
        numLength1 = len(twoDList[i][0])
        numLength2 = len(twoDList[i][2])
        
        equaLen.append(2 + max(numLength1, numLength2))
        
        dashes.append("-" * equaLen[i])
        
        if numLength1 >= numLength2:
            twoDList[i][0] = "  " + twoDList[i][0]
            addSpaces = equaLen[i] - 2 - numLength2
            twoDList[i][2] = twoDList[i][1] + " " + (" " * addSpaces) + twoDList[i][2]
        else:
            addSpaces = equaLen[i] - numLength1
            twoDList[i][0] = (" " * addSpaces) + twoDList[i][0]
            twoDList[i][2] = twoDList[i][1] + " " + twoDList[i][2]
            
        topNum.append(twoDList[i][0])
        bottomNum.append(twoDList[i][2])
            
        if show == True:
            if ReOp[i] == "+":
                tempAnswer = str(ReNum1[i] + ReNum2[i])
                answers.append(tempAnswer)
                addSpaces = equaLen[i] - len(answers[i])
                answers[i] = (" " * addSpaces) + answers[i]
            else:
                tempAnswer = str(ReNum1[i] - ReNum2[i])
                answers.append(tempAnswer)
                addSpaces = equaLen[i] - len(answers[i])
                answers[i] = (" " * addSpaces) + answers[i]

    
    
    topString = "    ".join(topNum)
    bottomString = "    ".join(bottomNum)
    dashesString = "    ".join(dashes)

    
    if show == True:
        answersString = "    ".join(answers)
        arranged_problems = topString + "\n" + bottomString + "\n" + dashesString + "\n" + answersString
    else:
        arranged_problems = topString + "\n" + bottomString + "\n" + dashesString
    
    
    return arranged_problems