t = int(input())

for _ in range(t):
    time_question = [int(x) for x in input().split()]
    points_of_question = [int(x) for x in input().split()]
    points_question = [[0]*2 for _ in range(3)]
    print(points_question)

    for i in range(3):
        points_question[i][0] = points_of_question[i] 
        points_question[i][1] = time_question[i]
    
    print(points_question)
    points_question.sort(reverse = True)
    if(points_question[0][0] == points_question[1][0] and points_question[0][1] > points_question[1][1]):
        points_question[0][1],points_question[1][1] = points_question[1][1],points_question[0][1]
    
    if(points_question[2][0] == points_question[1][0] and points_question[2][1] < points_question[1][1]):
            points_question[2][1],points_question[1][1] = points_question[1][1],points_question[2][1]
    
    print(points_question)

    time = 240
    points = 0
    
    questions_solved = time//points_question[0][1]
    if(questions_solved > 20):
        questions_solved = 20
    points += questions_solved*points_question[0][0]
    time -= points_question[0][1]*questions_solved
    print("time:",time)
    print("solved",questions_solved)
    print(points)
    
    questions_solved = time//points_question[1][1]
    if(questions_solved > 20):
        questions_solved = 20
    points += questions_solved*points_question[1][0]
    time -= points_question[1][1]*questions_solved
    print("time:",time)
    print("solved",questions_solved)
    print(points)
    
    questions_solved = time//points_question[2][1]
    if(questions_solved > 20):
        questions_solved = 20
    points += questions_solved*points_question[2][0]
    time -= points_question[2][1]*questions_solved
    print("time:",time)
    print("solved",questions_solved)
    
    print(points)