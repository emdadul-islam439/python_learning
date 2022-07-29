##How this line of code works->  
# for s in[*open(0)][1:]:print(0-abs(eval(s.replace(' ','-')))//-10)

#cut the solution in smaller part
# for s in[*open(0)][1:]:
#     replacedSpacedWithMinusStr = s.replace(' ','-') #what the 's' contains?
#     evalCalculation = eval(replacedSpacedWithMinusStr) #what eval() do?
#     absCalculation = abs(evalCalculation)
#     lastCalculation = 0-absCalculation//-10 #recheck //-10 part's output
#     print(lastCalculation)


#How this solution works->
for i in range(int(input())): #won't there be any 't' as input? later known tha range() function takes the 't' as input
    a,b = map(int,input().split()) #how the map() will assign the values to 'a,b'?
    print((abs(a-b)+9)//10) #this very much clear


###Most of the solution is clear to me->
# t=int(input())
# while(t):
#     t=t-1
#     a,b=map(int,input().split())  #how the map() working in this line
#     print((abs(a-b)+9)//10)


###How this works->
# for _ in range(int(input())):  #they used "_" (underScore) character, but where is the input 't'
#        a, b = map(int, input().split())  #how is map() working
#        print(0 - -abs(a-b)//10)  #now, it is clear to me


###this is answering some questions
# t = int(input())
# for _ in range(t):
#     a, b = map(int,input().split())
#     print((abs(a-b) + 9) // 10)