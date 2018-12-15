def recipeMaker(arr):

    LOOP_AMOUNT = 30121;
    RECIPE_SIZE = 10;

    counter = 0;
    initialLoopLength = len(arr);
    firstElfIndex = 0;
    secondElfIndex = 1;

    while( len(arr) < LOOP_AMOUNT + RECIPE_SIZE):
        total = arr[firstElfIndex] + arr[secondElfIndex];
        index = len(arr);
        print(total)
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

    result = (arr[LOOP_AMOUNT : RECIPE_SIZE + LOOP_AMOUNT]);
    return (''.join(str(recipe) for recipe in result))

print(recipeMaker([3,7]));
