
def coordinates(arr):
    marker = 1;
    storage = {};
    maxX = 0;
    maxY = 0;
    minY = 401;
    minX = 401;
    matrix = [[0]*400 for i in range(400)]
    for a in range(len(arr)):
        coord = arr[a].split();
        first = coord[0][:-1];
        second = coord[1];
        first = int(first);
        second = int(second);
        if first < minX:
            minX = first;
        if first > maxX:
            maxX = first;
        if second < minY:
            minY = second;
        if second > maxY:
            maxY = second;
        storage[marker] = [first, second];
        matrix[first][second] = marker

        marker += 1;

    for y in range(400):
        for x in range(400):
            flag = False;
            if x > maxX or x < minX or y > maxY or y < minY:
                flag = True;
            addedUp = 0;
            temp = [];
            bad = [];
            for keys, values in storage.items():
                
                xDist = abs(values[0] - x);
                yDist = abs(values[1] - y);
                total = xDist + yDist;
                addedUp += total;
                
            if addedUp < 10000:
                matrix[x][y] = '.';
            else:
                matrix[x][y] = '0';

            #print('F: ', first, ' S: ', second, ' INDEX: ', index)
    dict1 = {};
    region = 0;
    for y in range(400):
        for x in range(400):
            if matrix[x][y] == '.':
                region += 1;
                
    return region;

print(coordinates(["353, 177",
"233, 332",
"178, 231",
"351, 221",
"309, 151",
"105, 289",
"91, 236",
"321, 206",
"156, 146",
"94, 82",
"81, 114",
"182, 122",
"81, 153",
"319, 312",
"334, 212",
"275, 93",
"224, 355",
"347, 94",
"209, 65",
"118, 172",
"113, 122",
"182, 320",
"191, 178",
"99, 70",
"260, 184",
"266, 119",
"177, 178",
"313, 209",
"61, 285",
"155, 218",
"354, 198",
"274, 53",
"225, 138",
"228, 342",
"187, 165",
"226, 262",
"143, 150",
"124, 159",
"325, 210",
"163, 176",
"326, 91",
"170, 193",
"84, 265",
"199, 248",
"107, 356",
"45, 340",
"277, 173",
"286, 44",
"242, 150",
"120, 230"]));