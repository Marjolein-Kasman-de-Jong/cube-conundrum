from get_puzzle_input import games

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

# Create empty lists
list_of_games = []
list_of_impossible_games = []
list_of_possible_games = []

# Add existing games to list_of_games
for game in games:
    list_of_games.append(game['id'])

# Add impossible games to list_of_impossible_games
for game in games:
    for color_set in game['color_sets']:
        for key, value in color_set.items():
            if (key == 'red' and value > RED_CUBES) or (key == 'green' and value > GREEN_CUBES) or (key == 'blue' and value > BLUE_CUBES):
                list_of_impossible_games.append(game['id'])

# Add existing games that are not in list_of_impossible_games to list_of_possible_games
for game in list_of_games:
    if not game in list_of_impossible_games:
        list_of_possible_games.append(game)

# Add up numbers of possible games
sum = 0

for item in list_of_possible_games:
    sum += int(item)

print(sum)