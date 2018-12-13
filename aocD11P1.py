
def powerLevels(gridNumber):

    grid = [[0 for x in range(300)] for y in range(300)];

    for y in range(1, 300):
        
        for x in range(1, 300):
            rackID = x + 10;
            starting = rackID * y;
            addedSerial = starting + gridNumber;
            result = addedSerial * rackID;
            digit = (result // 100 % 10) - 5;
            grid[y][x] = digit;
        print(digit)
    maxCount = 0;
    finalX = 0;
    finalY = 0;
    for y in range(1, 298):
        for x in range(1, 298):
            
            total = grid[y][x] + grid[y][x+1] + grid[y][x+2] \
            + grid[y+1][x] + grid[y+1][x+1] + grid[y+1][x+2] \
            + grid[y+2][x] + grid[y+2][x+1] + grid[y+2][x+2];
            if total > maxCount:
                maxCount = total;
                finalX = x;
                finalY = y;
            
    return (finalX, finalY)

print(powerLevels(7989));
