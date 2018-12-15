
def plantGenerations(arr):
    stages = {};
    for a in arr:
        if len(a) > 15:
            data = a.split();
            initial = data[2];
        else:
            data = a.split();
            stages[data[0]] = data[2];
    
    initialList = list(initial);
    deadList = list(initial);
    for a in range(20):
        counter = 0;
        while (counter < len(initialList) - 5):
            check = initialList[counter] + initialList[counter+1] + initialList[counter+2] \
            + initialList[counter+3] + initialList[counter+4];
            #print(check);
            if check in stages:
                initialList[counter+2] = stages[check];
                #counter += 4;
            counter += 1;
    print(initialList);
    print(deadList);

    points = 0;
    for b in range(len(initialList)):
        if initialList[b] == '#':
            points += b;
    return points



# print(plantGenerations(["initial state: ...#..#.#..##......###...###...........",
# "...## => #",
# "..#.. => #",
# ".#... => #",
# ".#.#. => #",
# ".#.## => #",
# ".##.. => #",
# ".#### => #",
# "#.#.# => #",
# "#.### => #",
# "##.#. => #",
# "##.## => #",
# "###.. => #",
# "###.# => #",
# "####. => #"]));

print(plantGenerations(["initial state: #........#.#.#...###..###..###.#..#....###.###.#.#...####..##..##.#####..##...#.#.....#...###.#.####",
"#..## => .",
"##..# => #",
"..##. => .",
".##.# => #",
"..... => .",
"..### => #",
"###.# => #",
"#.... => .",
"#.##. => #",
".#.## => #",
"#...# => .",
"...## => .",
"###.. => #",
".#..# => .",
"####. => .",
"....# => .",
"##### => #",
".###. => .",
"#..#. => .",
"##... => #",
".#... => #",
"#.#.# => .",
"..#.. => #",
"...#. => #",
"##.#. => .",
".##.. => #",
".#.#. => .",
"#.#.. => .",
"..#.# => #",
"#.### => .",
"##.## => .",
".#### => #"]));