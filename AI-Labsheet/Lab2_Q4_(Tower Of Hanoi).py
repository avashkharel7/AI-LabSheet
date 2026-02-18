def move_disk(state, from_rod, to_rod):

    new_state = [list(rod) for rod in state]

    if not new_state[from_rod]:
        return None

    disk = new_state[from_rod][-1]

    if new_state[to_rod] and new_state[to_rod][-1] < disk:
        return None

    new_state[from_rod].pop()
    new_state[to_rod].append(disk)

    return tuple(tuple(rod) for rod in new_state)


def dfs(state, goal, visited):

    if state == goal:
        return True

    visited.add(state)

    for i in range(3):
        for j in range(3):
            if i != j:
                new_state = move_disk(state, i, j)

                if new_state and new_state not in visited:
                    print("Move:", state, "→", new_state)

                    if dfs(new_state, goal, visited):
                        return True

    return False


# Initial and goal state
initial = ((3,2,1), (), ())
goal = ((), (), (3,2,1))

visited = set()
dfs(initial, goal, visited)
