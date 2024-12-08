VISITED = 'VISITED'
OBSTICLE = 'OBSTICLE'

UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)

next_dir = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}

DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def create_map_and_find_start():
    data = read_file("./input_folder/day_6_input.txt")
    map_of_factory = [[] for x in data]
    starting_pos = (0, 0)

    for i in range(len(data)): 
        for j in range(len(data[i])): 
            square = data[i][j]
            if square == '.':
                map_of_factory[i].append("")
            elif square == '#':
                map_of_factory[i].append(OBSTICLE)
            else:
                map_of_factory[i].append(VISITED)
                starting_pos = (i, j)
    
    return map_of_factory, starting_pos

def is_legal_move(next_pos, factory_map):
    if next_pos[0] >= 0 and next_pos[0] < len(factory_map) and next_pos[1] >= 0 and next_pos[1] < len(factory_map[0]):
        if factory_map[next_pos[0]][next_pos[1]] != OBSTICLE:
            return True
    return False

def leaving_map(next_pos, factory_map):
    if next_pos[0] < 0 or next_pos[0] >= len(factory_map) or next_pos[1] < 0 or next_pos[1] >= len(factory_map[0]):
        return True
    return False

# Traverse the map and detect if there is a loop
def traverse_map(start_pos, factory_map):
    the_traversed_map = factory_map
    not_done = True
    current_pos = start_pos
    current_dir = UP
    visited_positions = set()  # Track (position, direction) pairs to detect loops
    
    while not_done:
        next_pos = (current_pos[0] + current_dir[0], current_pos[1] + current_dir[1])
        
        # Check if the guard leaves the map
        if leaving_map(next_pos, factory_map):
            not_done = False
        
        # Check if the move is legal
        elif is_legal_move(next_pos, factory_map):
            current_pos = next_pos
            # Check if the position and direction are revisited (i.e., we have a loop)
            if (current_pos, current_dir) in visited_positions:
                return True  # Loop detected
            
            visited_positions.add((current_pos, current_dir))
            # Mark the square as visited
            if the_traversed_map[current_pos[0]][current_pos[1]] == "":
                the_traversed_map[current_pos[0]][current_pos[1]] = VISITED
        
        else:
            # Change direction if the move is not legal
            current_dir = next_dir[current_dir]
    
    return False  # No loop detected

# Count the number of loop-creating obstacle placements
def count_loop_creating_obstacles():
    the_map, start_pos = create_map_and_find_start()
    loop_count = 0

    # Iterate over all positions in the map
    for i in range(len(the_map)):
        for j in range(len(the_map[i])):
            if (i, j) != start_pos and the_map[i][j] != OBSTICLE:
                # Temporarily place an obstacle at (i, j)
                the_map[i][j] = OBSTICLE
                # Check if placing the obstacle creates a loop
                if traverse_map(start_pos, the_map):
                    loop_count += 1
                # Remove the obstacle
                the_map[i][j] = ""

    print(f"Total placements that create a loop: {loop_count}")

# Run the part 2 function
count_loop_creating_obstacles()
