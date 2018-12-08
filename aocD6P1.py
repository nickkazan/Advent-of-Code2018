
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
            closest = 100000;
            temp = [];
            bad = [];
            for keys, values in storage.items():
                
                xDist = abs(values[0] - x);
                yDist = abs(values[1] - y);
                total = xDist + yDist;
                if total <= closest:
                    closest = total;
                    index = keys;
                    #first = values[0];
                    #second = values[1];
                    temp.append(closest);
            if flag:
                bad.append(index);
            if temp.count(closest) > 1 or index in bad:
                matrix[x][y] = '.'
            else:
                matrix[x][y] = index;

            #print('F: ', first, ' S: ', second, ' INDEX: ', index)
    dict1 = {};
    total = 0;
    for y in range(400):
        for x in range(400):
            if matrix[x][y] == '.' or matrix[x][y] in bad:
                pass;
            elif matrix[x][y] in dict1:
                dict1[matrix[x][y]] += 1;
            else:
                dict1[matrix[x][y]] = 1;

    for key, value in dict1.items():
        if value > 10000:
            pass;
        else:
            if value > total:
                total = value;
                
    return total;

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