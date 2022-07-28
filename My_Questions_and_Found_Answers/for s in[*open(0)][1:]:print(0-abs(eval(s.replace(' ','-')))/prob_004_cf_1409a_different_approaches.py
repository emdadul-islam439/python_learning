##How this line of code works->  
# for s in[*open(0)][1:]:print(0-abs(eval(s.replace(' ','-')))//-10)

for s in[*open(0)][1:]:
    lineBeforeEval = s.replace(' ','-')
    lineBeforeAbs = eval(lineBeforeEval)
    beforeLastCalculation = abs(lineBeforeAbs)
    lastCalculation = 0-beforeLastCalculation//-10
    print(lastCalculation)