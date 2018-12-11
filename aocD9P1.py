def marbleGame(string):

    marbles = [];
    info = string.split();
    totalPlayers = int(info[0]);
    players = [0] * totalPlayers;
    lastMarble = int(info[6]);
    playerIndex = 0;
    currentMarble = 0;
    marbleIndex = 0;

    while currentMarble <= lastMarble:
        #print(marbles)
        if currentMarble % 23 == 0 and currentMarble != 0:
            players[playerIndex] += currentMarble;
            marbleIndex -= 9;
            if marbleIndex < 0:
                marbleIndex = marbles.index(marbles[marbleIndex]);
            popped = marbles.pop(marbleIndex);
            #currentMarble = marbles[marbleIndex];
            players[playerIndex] += popped;
            playerIndex += 1;
            currentMarble += 1;
            marbleIndex += 2;
        # elif marbleIndex :
        #     print('DONKEY')
        #     marbles.append(currentMarble);
        #     marbleIndex += 2;
        #     currentMarble += 1;
        #     playerIndex += 1;
        elif marbleIndex > len(marbles):
            marbleIndex = 1;
            marbles.insert(marbleIndex, currentMarble);
            marbleIndex += 2;
            playerIndex += 1;
            currentMarble += 1;
        else:
            marbles.insert(marbleIndex, currentMarble);
            marbleIndex += 2;
            playerIndex += 1;
            currentMarble += 1;
        if playerIndex >= totalPlayers:
            playerIndex = 0;

    #print(marbles)
    #print(players)
    return max(players)

print(marbleGame('424 players; last marble is worth 71482 points'));