#N, S, E, W == 0, 1, 2, 3

n = int(input())
x, y = 0, 0

for i in range (n):
    c_dir, dist = tuple(input().split())
    dist = int(dist)

    dir_map = {
        'E' : 0,
        'S' : 1,
        'W' : 2,
        'N' : 3
    }
    dir_num = dir_map[c_dir]

    
    ''' if c_dir == 'E':
        dir_num = 0
    elif c_dir == 'S':
        dir_num = 1
    elif c_dir == "W":
        dir_num = 2
    elif c_dir == 'N':
        dir_num = 3 '''
    
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    #dir_num 방향으로 dist 만큼 이동한 최종 위치
    x, y = x + dx[dir_num] * dist, y + dy[dir_num] * dist
print(x,y)