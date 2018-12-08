def graphTraversal(arr):
    
    #Create the graph using a dictionary and lists
    graph = {};
    result = '';
    final = True;
    check = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    lastLetterFinder = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
    for a in range(len(arr)):
        parsed = arr[a].split();
        first = parsed[1];
        second = parsed[7];
        if first not in graph.keys():
            graph[first] = [];
        graph[first].append(second);
    for key in graph.keys():
        if key in lastLetterFinder:
            lastLetterFinder.remove(key);
        
    while final:
        letterIndex = 0;
        while letterIndex < len(check):
            flag = True;
            for b in graph.values():
                if check[letterIndex] in b:
                    flag = False;
                    break;
            if flag:
                if check[letterIndex] in graph:
                    print('Dealing with: ', check[letterIndex]);
                    if check[letterIndex] not in result:
                        result += check[letterIndex];
                    print('POPPED: ', graph.pop(check[letterIndex]))
                    check
                    letterIndex = 0;
                else:
                    letterIndex += 1
            else:
                letterIndex += 1;

        if len(graph) < 1:
            final = False;
    
    result += lastLetterFinder[0]
    return result;



print(graphTraversal(["Step J must be finished before step E can begin.",
"Step X must be finished before step G can begin.",
"Step D must be finished before step A can begin.",
"Step K must be finished before step M can begin.",
"Step P must be finished before step Z can begin.",
"Step F must be finished before step O can begin.",
"Step B must be finished before step I can begin.",
"Step U must be finished before step W can begin.",
"Step A must be finished before step R can begin.",
"Step E must be finished before step R can begin.",
"Step H must be finished before step C can begin.",
"Step O must be finished before step S can begin.",
"Step Q must be finished before step Y can begin.",
"Step V must be finished before step W can begin.",
"Step T must be finished before step N can begin.",
"Step S must be finished before step I can begin.",
"Step Y must be finished before step W can begin.",
"Step Z must be finished before step C can begin.",
"Step M must be finished before step L can begin.",
"Step L must be finished before step W can begin.",
"Step N must be finished before step I can begin.",
"Step I must be finished before step G can begin.",
"Step C must be finished before step G can begin.",
"Step G must be finished before step R can begin.",
"Step R must be finished before step W can begin.",
"Step Z must be finished before step R can begin.",
"Step Z must be finished before step N can begin.",
"Step G must be finished before step W can begin.",
"Step L must be finished before step G can begin.",
"Step Y must be finished before step R can begin.",
"Step P must be finished before step I can begin.",
"Step C must be finished before step W can begin.",
"Step T must be finished before step G can begin.",
"Step T must be finished before step R can begin.",
"Step V must be finished before step Z can begin.",
"Step L must be finished before step C can begin.",
"Step K must be finished before step I can begin.",
"Step J must be finished before step I can begin.",
"Step Q must be finished before step C can begin.",
"Step F must be finished before step A can begin.",
"Step H must be finished before step Y can begin.",
"Step M must be finished before step N can begin.",
"Step P must be finished before step H can begin.",
"Step M must be finished before step C can begin.",
"Step V must be finished before step Y can begin.",
"Step O must be finished before step V can begin.",
"Step O must be finished before step Q can begin.",
"Step A must be finished before step G can begin.",
"Step T must be finished before step Z can begin.",
"Step K must be finished before step R can begin.",
"Step H must be finished before step O can begin.",
"Step O must be finished before step Y can begin.",
"Step O must be finished before step C can begin.",
"Step K must be finished before step P can begin.",
"Step P must be finished before step F can begin.",
"Step E must be finished before step M can begin.",
"Step M must be finished before step I can begin.",
"Step T must be finished before step W can begin.",
"Step P must be finished before step L can begin.",
"Step A must be finished before step O can begin.",
"Step X must be finished before step V can begin.",
"Step S must be finished before step G can begin.",
"Step A must be finished before step Y can begin.",
"Step J must be finished before step R can begin.",
"Step K must be finished before step F can begin.",
"Step J must be finished before step A can begin.",
"Step P must be finished before step C can begin.",
"Step E must be finished before step N can begin.",
"Step F must be finished before step Y can begin.",
"Step J must be finished before step D can begin.",
"Step H must be finished before step Z can begin.",
"Step U must be finished before step H can begin.",
"Step J must be finished before step T can begin.",
"Step V must be finished before step G can begin.",
"Step Z must be finished before step I can begin.",
"Step H must be finished before step W can begin.",
"Step B must be finished before step R can begin.",
"Step F must be finished before step B can begin.",
"Step X must be finished before step C can begin.",
"Step L must be finished before step R can begin.",
"Step F must be finished before step U can begin.",
"Step D must be finished before step N can begin.",
"Step P must be finished before step O can begin.",
"Step B must be finished before step O can begin.",
"Step F must be finished before step C can begin.",
"Step H must be finished before step L can begin.",
"Step O must be finished before step N can begin.",
"Step J must be finished before step Y can begin.",
"Step H must be finished before step N can begin.",
"Step O must be finished before step L can begin.",
"Step I must be finished before step W can begin.",
"Step J must be finished before step H can begin.",
"Step D must be finished before step Z can begin.",
"Step F must be finished before step W can begin.",
"Step X must be finished before step W can begin.",
"Step Y must be finished before step M can begin.",
"Step T must be finished before step M can begin.",
"Step U must be finished before step G can begin.",
"Step L must be finished before step I can begin.",
"Step N must be finished before step W can begin.",
"Step E must be finished before step C can begin."]));