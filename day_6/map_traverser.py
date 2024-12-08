VISITED = 'VISITED'
OBSTACLE = 'OBSTACLE'

UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)

next_dir = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def create_map_and_find_start():
    data = read_file("./input_folder/day_6_input.txt")
    map_of_factory = [[] for _ in data]
    starting_pos = (0, 0)

    for i in range(len(data)):
        for j in range(len(data[i])):
            square = data[i][j]
            if square == '.':
                map_of_factory[i].append("")
            elif square == '#':
                map_of_factory[i].append(OBSTACLE)
            else:
                map_of_factory[i].append(VISITED)
                starting_pos = (i, j)

    return map_of_factory, starting_pos

def is_legal_move(next_pos, factory_map):
    return (
        0 <= next_pos[0] < len(factory_map)
        and 0 <= next_pos[1] < len(factory_map[0])
        and factory_map[next_pos[0]][next_pos[1]] != OBSTACLE
    )

def leaving_map(next_pos, factory_map):
    return not (0 <= next_pos[0] < len(factory_map) and 0 <= next_pos[1] < len(factory_map[0]))

def traverse_map(start_pos, factory_map):
    not_done = True
    current_pos = start_pos
    current_dir = UP
    visited_positions = set()
    visited_positions.add((current_pos, current_dir))

    while not_done:
        next_pos = (current_pos[0] + current_dir[0], current_pos[1] + current_dir[1])

        if leaving_map(next_pos, factory_map):
            not_done = False
        elif is_legal_move(next_pos, factory_map):
            current_pos = next_pos
            map_location = factory_map[current_pos[0]][current_pos[1]]

            if (current_pos, current_dir) in visited_positions:
                return factory_map, True  # Loop detected

            visited_positions.add((current_pos, current_dir))

            if map_location == "":
                factory_map[current_pos[0]][current_pos[1]] = VISITED
        else:
            current_dir = next_dir[current_dir]

    return factory_map, False

def solve():
    the_map, start_pos = create_map_and_find_start()
    traversed_map, _ = traverse_map(start_pos, the_map)

    visited_counter = sum(row.count(VISITED) for row in traversed_map)
    print(f"Visited squares: {visited_counter}")

def count_loop_creating_obstacles():
    original_map, start_pos = create_map_and_find_start()
    loop_count = 0

    for i in range(len(original_map)):
        for j in range(len(original_map[i])):
            if (i, j) == start_pos or original_map[i][j] == OBSTACLE:
                continue

            test_map, _ = create_map_and_find_start()
            test_map[i][j] = OBSTACLE

            _, is_loop = traverse_map(start_pos, test_map)
            if is_loop:
                loop_count += 1

    print(f"Total placements that create a loop: {loop_count}")

if __name__ == "__main__":
    solve()
    count_loop_creating_obstacles()
