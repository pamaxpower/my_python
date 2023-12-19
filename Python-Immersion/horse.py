from collections import deque

def count_knight_moves(start, n):
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    queue = deque([(start, 0)])
    visited = set([start])
    cell_list = []

    while queue:
        current, moves = queue.popleft()

        if moves == n:
            return len(visited)

        x, y = current

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            next_cell = (nx, ny)

            if 0 <= nx < 3 and 0 <= ny < 6 and next_cell not in visited:
                queue.append((next_cell, moves + 1))
                visited.add(next_cell)
                cell = (next_cell[0])*6 + next_cell[1]
                cell_list.append(cell)

        print(cell_list)
    return 0

start = (0, 0)  # начальная клетка
n = 3  # количество шагов

print(count_knight_moves(start, n))