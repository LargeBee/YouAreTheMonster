#Base Features
width = 15
height = 15
features = {'floor': '.', 'wall': '#', 'entrance': 'S', 'exit': 'F'}
algos = {'block': 0, 'cell': 1}

#Block Aggregation Options


#Cellular Automata Options


#Choose Algorithm
algo = algos['cell']

command = ''

while not command == 'q':
    #Generate and display map
    print('What would you like to do?')
    command = input('(g)enerate new map, (q)uit, (s)ave: ')
    