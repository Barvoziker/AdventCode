## Hand shape : [Win, Draw, Lose]
## X is Rock
## Y is Paper
## Z is Scissors
a = {
    "X": ["C", "A", "B"],
    "Y": ["A", "B", "C"],
    "Z": ["B", "C", "A"],
}

## Hand shape : [Win, Draw, Lose]
## A is Rock
## B is Paper
## C is Scissors
b = {
    "A" : ["Z", "X", "Y"],
    "B" : ["X", "Y", "Z"],
    "C" : ["Y", "Z", "X"],
}


with open ("input.txt") as f: ## Open the file
    data = f.read().splitlines() ## split on newlines
    
    ## Part 1
    s = 0 ## init score to 0
    for l in data: ## for each line
        x, y = l.split(" ") ## split on space
        n = a[y].index(x) ## get the index of the hand shape in the dict
        if n == 0: ## if the index is 0, it's a win
            s += 6
        if n == 1: ## if the index is 1, it's a draw
            s += 3
        if y == "X": ## point bonus for X
            s += 1
        if y == "Y": ## point bonus for Y
            s += 2
        if y == "Z": ## point bonus for Z
            s += 3;
    print(s)

    ##Part 2
    s = 0 ## init score to 0
    for l in data: ## for each line
        x, y = l.split(" ") ## split on space
        if y == "X":
            g = 0
        if y == "Y":
            g = 1
            s += 3
        if y == "Z":
            g = 2
            s += 6
        y = b[x][g]
        if y == "X":
            s += 1
        if y == "Y":
            s += 2
        if y == "Z":
            s += 3
    print(s)


