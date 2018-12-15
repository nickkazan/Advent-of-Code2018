def recipeMaker(arr):

    LOOP_TEST = [0,3,0,1,2,1];
    LOOP_TEST2 = [9,2,5,1,0];
    LOOP_TEST3 = [5,9,4,1,4];

    counter = 0;
    firstElfIndex = 0;
    secondElfIndex = 1;

    while( True ):
        total = arr[firstElfIndex] + arr[secondElfIndex];
        index = len(arr);
        if total == 0:
            arr.append(0)
        while(total != 0):
            digit = total % 10;
            total = total // 10;
            arr.insert(index, digit);
        firstElfIndex = (firstElfIndex + 1 + arr[firstElfIndex])
        secondElfIndex = (secondElfIndex + 1 + arr[secondElfIndex])
        if firstElfIndex >= len(arr):
            firstElfIndex = firstElfIndex - len(arr);
            if firstElfIndex >= len(arr):
                firstElfIndex = firstElfIndex - len(arr);
        if secondElfIndex >= len(arr):
            secondElfIndex = secondElfIndex - len(arr);
            if secondElfIndex >= len(arr):
                secondElfIndex = secondElfIndex - len(arr);
        if arr[-6:] == LOOP_TEST:
            sub = 6;
            break;
        elif arr[-7: -1] == LOOP_TEST:
            sub = 7;
            break;
    result = len(arr) - sub;
    return result;

print(recipeMaker([3,7]));
