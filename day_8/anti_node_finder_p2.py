def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def dict_key_from_coords(coord_tuple):
    return f'{coord_tuple[0]}_{coord_tuple[1]}'

def coords_from_dict_key(dict_key):
    return tuple(map(int, dict_key.split('_')))

def antennas_coord_dict(data):
    antennas = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != '.': 
                if data[i][j] not in antennas:
                    antennas[data[i][j]] = []
                antennas[data[i][j]].append((i, j))
    return antennas

def create_grid(data):
    grid = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            grid[dict_key_from_coords((i, j))] = {"antenna": data[i][j], "anti_nodes": []}      
    return grid

def distance_with_dir(coord1, coord2):
    return coord1[0] - coord2[0], coord1[1] - coord2[1]

def is_within_grid(coord, dimensions):
    return 0 <= coord[0] < dimensions[0] and 0 <= coord[1] < dimensions[1]

def anti_node_in_direction(coord, direction):
    x, y = coord
    x_dir, y_dir = direction
    x += x_dir
    y += y_dir
    return (x, y)

def place_and_count_anti_nodes_locations(grid, antennas, dimensions):
    for frequency, antenna_list in antennas.items():
        for i in range(len(antenna_list)):
            for j in range(i + 1, len(antenna_list)):
                c1, c2 = antenna_list[i], antenna_list[j]
                # Need to include the antenna antinodes as well
                grid[dict_key_from_coords(c1)]["anti_nodes"].append(c2)
                grid[dict_key_from_coords(c2)]["anti_nodes"].append(c1)
                             
                # Direction and distance
                dx, dy = c2[0] - c1[0], c2[1] - c1[1]
                # 2x the distance from a1 towards a2
                antinode1 = (c1[0] - dx, c1[1] - dy)
                # 2x the distance from a2 towards a1
                antinode2 = (c2[0] + dx, c2[1] + dy)
                
                while is_within_grid(antinode1, dimensions) or is_within_grid(antinode2, dimensions):
                    if is_within_grid(antinode1, dimensions):
                        grid[dict_key_from_coords(antinode1)]["anti_nodes"].append(antinode2)
                    if is_within_grid(antinode2, dimensions):
                        grid[dict_key_from_coords(antinode2)]["anti_nodes"].append(antinode1)
                    antinode1 = (antinode1[0] - dx, antinode1[1] - dy)
                    antinode2 = (antinode2[0] + dx, antinode2[1] + dy)        
    total = 0              
    for key in grid:
        if len(grid[key]["anti_nodes"]) > 0:
            total += 1
    return total
                    
def solve():
    data = read_file('input_folder/day_8_input.txt')
    antennas = antennas_coord_dict(data)
    grid = create_grid(data)
    dimensions = (len(data), len(data[0]))
    total = place_and_count_anti_nodes_locations(grid, antennas, dimensions)
    print(total)
    
solve()