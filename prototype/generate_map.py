#Imports
from datetime import datetime

#Base Features
width = 60
height = 60
features = {'floor': '.', 'wall': '#', 'entrance': 'S', 'exit': 'F'}
algos = {'block': 0, 'cell': 1}

#Block Aggregation Options


#Cellular Automata Options


#Choose Algorithm
algo = algos['cell']

command = ''
game_map = ''

def save_map_to_file():
    current_datetime = str(datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
    file_name = f'{current_datetime}.txt'
    with open(file_name, 'w') as f:
        for y in range(height):
            for x in range(width):
                f.write(game_map[(width * y) + x])
            f.write('\n')

def generate_map():
    pass

while not command == 'q':
    #Make map from 0s and 1s
    game_map = generate_map()
    #For every 0 put floor and every 1 put wall (or vice versa)
    #Find a start spot
    print('What would you like to do?')
    command = input('(g)enerate new map, (s)ave and generate new map, (q)uit: ')
    if command == 's':
        save_map_to_file()