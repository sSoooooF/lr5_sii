import heapq

def a_star(grid, start, goal, obstacles=None):
    if obstacles is None:
        obstacles = grid.obstacles

    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            break

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next = current[0] + dx, current[1] + dy
            if grid.is_valid(next[0], next[1], obstacles):
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + abs(next[0] - goal[0]) + abs(next[1] - goal[1])
                    heapq.heappush(open_list, (priority, next))
                    came_from[next] = current

    # Reconstruct the path
    if goal not in came_from:
        return []

    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path
