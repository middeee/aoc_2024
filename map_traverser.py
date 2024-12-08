VISITED = 'VISITED'
OBSTICLE = 'OBSTICLE'

UP = (-1,0)
RIGHT = (0,1)
DOWN = (1,0)
LEFT = (0,-1)

next_dir = {UP:RIGHT, RIGHT:DOWN, DOWN:LEFT, LEFT: UP}


DIRECTIONS = [UP,RIGHT,DOWN,LEFT]

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def create_map_and_find_start():
    data = read_file("./inputs_folder/day_6_input.txt")
    map_of_factory = [[] for x in data]
    starting_pos = (0,0)

    for i in range(len(data)): 
        for j in range(len(data[i])): 
            square = data[i][j]
            if square == '.':
                map_of_factory[i].append("")
            elif square == '#':
                map_of_factory[i].append(OBSTICLE)
            else:
                map_of_factory[i].append(VISITED)
                starting_pos = (i,j)
    
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

def traverse_map(start_pos, factory_map):
    the_traversed_map = factory_map
    not_done = True
    current_pos = start_pos
    current_dir = UP
    while(not_done):
        next_pos = (current_pos[0] + current_dir[0], current_pos[1] + current_dir[1])
        if leaving_map(next_pos, factory_map):
            not_done = False
        elif is_legal_move(next_pos, factory_map):
            current_pos = next_pos
            map_location = the_traversed_map[current_pos[0]][current_pos[1]]
            if map_location == "":
                the_traversed_map[current_pos[0]][current_pos[1]] = VISITED

        else: 
            current_dir = next_dir[current_dir]

    return the_traversed_map
            

def solve():
    the_map, start_pos = create_map_and_find_start()
    traversed_map = traverse_map(start_pos, the_map)
    visited_counter = 0
    for row in traversed_map:
        for elem in row:
            if elem == VISITED:
                visited_counter += 1

    print(f"Visited squares: {visited_counter}")

solve()
