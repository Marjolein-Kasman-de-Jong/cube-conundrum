PUZZLE_INPUT = 'puzzle_input.txt'

# Creates a list of game dictionaries
games = []

with open(PUZZLE_INPUT) as file_object:
    for line in file_object:
        line = line.strip()
        # Creates a game dictionary
        game = {}
        # Adds game id to game dictionary
        line = line.split(':')
        game['id'] = line[0].split()[1]
        # Creates a list of color sets
        list_of_color_sets = []
        color_sets = line[1].split(';')
        for color_set in color_sets:
            # Creates a color set
            color_set_dict = {}
            color_set = color_set.split(',')
            for color in color_set:
                color = color.strip() 
                color = color.split(' ')
                key = color[1]
                value = color[0]
                color_set_dict[key] = int(value)
            # Adds color set to list of color sets    
            list_of_color_sets.append(color_set_dict)
        # Adds list of color sets to game dictionary
        game['color_sets'] = list_of_color_sets
        # Adds game dictionary to list of game dictionaries
        games.append(game)