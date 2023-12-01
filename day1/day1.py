file = 'day1.txt'
def part1():
    with open('day1.txt') as f:
        lines = f.readlines()

    total_sum = 0
    for line in lines:
        digits = [int(char) for char in line if char.isdigit()]
        value = digits[0] * 10 + digits[-1]
        total_sum += value
    print(total_sum)
    
def part2():
    lines = open("day1.txt").read().strip().split()
    sum = 0
    for i in range(len(lines)):
        x = lines[i]
        y = ""
        for i in range(len(x)):
            if x[i] in "0123456789":
                y += x[i]
            words = {"zero": 0,"one": 1 ,"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
                     "eight": 8, "nine": 9}
            for j in words:
                if x[i:i+len(j)] == j:
                    y += str(words.get(j))
            
        sum+= int(y[0]+y[-1])
    print(sum)
part1()
part2()