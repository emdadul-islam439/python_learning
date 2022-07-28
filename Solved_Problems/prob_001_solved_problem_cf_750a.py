inputString = input()
splitStringList = inputString.split()
n = int(splitStringList[0])
k = int(splitStringList[1])
needed_time = 5
remaining_time = 240
no_of_solved_problem = 0

while(True):
    remaining_time -= needed_time
    if(remaining_time < k): 
        break
    no_of_solved_problem += 1
    needed_time += 5

print(min(no_of_solved_problem, n))