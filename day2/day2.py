from collections import defaultdict
file = "/Users/abeporschet/personalProjects/aoc23/day2/day2.txt"
#only 12 red cubes, 13 green cubes, and 14 blue cubes
def partOne():
    lines = open(file).read().strip()
    maxBalls = {"red": 12, "green": 13, "blue": 14}
    count = 0
    for line in lines.split("\n"):
        possible = True #needed this inside the outer for loop to reset each time
        ID, line = line.split(':') #Turns out I needed the Game ID
        ID = int(ID.replace('Game ',''))
        for turn in line.split(";"):
            for balls in turn.split(','):
                num, col = balls.split()
                if int(num) > maxBalls.get(col,0):
                    possible = False
        if possible:
            count+= int(ID)
    print(count)
    
def partTwo():
    lines = open(file).read().strip()
    count = 0
    for line in lines.split("\n"):
        line = line.split(':')[1]
        dd = defaultdict(int)
        for turn in line.split(";"):
            for balls in turn.split(','):
                num, col = balls.split()
                dd[col]=max(dd[col], int(num)) 
            mult = 1
            print(dd)
        for v in dd.values():
            mult*=v
        count+=mult
    print(count)
partOne()
partTwo()