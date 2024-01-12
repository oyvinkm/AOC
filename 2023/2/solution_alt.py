sum_possible = 0
sum_powers = 0
limit = {'red': 12, 'green': 13, 'blue': 14}
 
with open('input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        impossible = False
        min_possible = {'red': 0, 'green': 0, 'blue': 0}
        picks = line.strip()[line.find(':')+2:].split('; ')
        for p in picks:
            for part in p.split(', '):
                #print(part)
                num, colour = part.split(' ')
                num = int(num)
                # part 1
                if num > limit[colour]:
                    impossible = True
                # part 2
                min_possible[colour] = max(min_possible[colour], num)
        if not impossible:
            sum_possible += (i+1)
        power = 1
        for v in min_possible.values():
            power *= v
        sum_powers += power
 
# part 1
print(sum_possible)
print(sum_powers)