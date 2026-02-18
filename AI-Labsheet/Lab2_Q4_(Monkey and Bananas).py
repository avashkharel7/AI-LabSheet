from collections import deque

# Initial State
initial_state = ('A', 'B', 'on_floor', False)

# Banana position
banana_position = 'C'

def goalTest(state):
    return state[3] == True


def get_successors(state):
    monkey_pos, box_pos, status, has_banana = state
    successors = []

    # Move monkey
    if status == 'on_floor':
        for pos in ['A', 'B', 'C']:
            if pos != monkey_pos:
                successors.append((pos, box_pos, 'on_floor', has_banana))

    # Push box
    if monkey_pos == box_pos and status == 'on_floor':
        for pos in ['A', 'B', 'C']:
            if pos != monkey_pos:
                successors.append((pos, pos, 'on_floor', has_banana))

    # Climb box
    if monkey_pos == box_pos and status == 'on_floor':
        successors.append((monkey_pos, box_pos, 'on_box', has_banana))

    # Grab banana
    if monkey_pos == banana_position and box_pos == banana_position and status == 'on_box':
        successors.append((monkey_pos, box_pos, 'on_box', True))

    return successors


def bfs():
    queue = deque([[initial_state]])
    visited = set()

    while queue:
        path = queue.popleft()
        state = path[-1]

        if goalTest(state):
            return path

        if state not in visited:
            visited.add(state)

            for successor in get_successors(state):
                new_path = list(path)
                new_path.append(successor)
                queue.append(new_path)

    return None


solution = bfs()

if solution:
    print("Solution Found:\n")
    for step in solution:
        print(step)
else:
    print("No Solution")
