def solution(n, plan):
    x, y = 1, 1
    moving = ['L', 'R', 'U', 'D']
    move_value = [-1, 1, -1, 1]
    move_plan = plan.split()
    
    for i in move_plan:
        for q in range(len(moving)):
            if i == moving[q]:
                if q <= 1:
                    ny = move_value[q]
                else:
                    nx = move_value[q]
            if (1 <= x + nx >= n) and (1 <= x + ny >= n):
                x += nx
                y += ny
    print(x,y)
    
    solution(5, 'R R R U D D')