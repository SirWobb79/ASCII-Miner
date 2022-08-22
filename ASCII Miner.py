print("<ASCII Miner 1.0>\n\nWASD: Move\nU: Upgrade\nR: Reset map\n\nYou: >\nBlocks: @\nNothing: .\n")

mine = [["@"for a in range(11)]for b in range(11)]

player = ">"
empty = "."

x = 5
y = 0

cash = 0
income = 1

price = 20
upgrade = 1

mine[y][x] = player
 
game = True

while game == True:

    print("----------------------\nYou earn $", income,"per block\n----------------------\nYou have $", cash, "\n----------------------\nUpgrade", upgrade, "is $", price, "\n----------------------")
    
    for i in mine:
        print(" ".join(i))
        
    action = input(">")
    
    if action == "s":
        y += 1
        if mine[y][x] == empty:
            y -= 1
            mine[y][x] = empty
            y += 1
            mine[y][x] = "v"
        else:
            y -= 1
            mine[y][x] = empty
            y += 1
            mine[y][x] = "v"
            cash += income
        
    if action == "a":
        x -= 1
        if mine[y][x] == empty:
            x += 1
            mine[y][x] = empty
            x -= 1
            mine[y][x] = "<"
        else:
            x += 1
            mine[y][x] = empty
            x -= 1
            mine[y][x] = "<"
            cash += income
        
    if action == "d":
        x += 1
        if mine[y][x] == empty:
            x -= 1
            mine[y][x] = empty
            x += 1
            mine[y][x] = ">"
        else:
            x -= 1
            mine[y][x] = empty
            x += 1
            mine[y][x] = ">"
            cash += income
    
    if action == "w":
        y -= 1
        if mine[y][x] == empty:
            y += 1
            mine[y][x] = empty
            y -= 1
            mine[y][x] = "^"
        else:
            y += 1
            mine[y][x] = empty
            y -= 1
            mine[y][x] = "^"
            cash += income
            
    if action == "u":
        if cash >= price:
            upgrade += 1
            cash -= price
            price *= 2
            income += 3
    
    if action == "r":
        mine = [["@"for a in range(11)]for b in range(11)]
        
        x = 5
        y = 0
        
        mine[y][x] = player
        print("Map has been reset")