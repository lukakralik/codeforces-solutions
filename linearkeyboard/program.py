t = int(input())

def search(keyboard, letter):
    for i in range(len(keyboard)):
        if keyboard[i] == letter:
            return i
    return 0

for i in range(t):
    keyboard = input()
    query = input()
    power = 0
    for i in range(len(query)):
        if i + 1 < len(query):
            power += abs(search(keyboard, query[i]) - search(keyboard, query[i+1]))
    print(power)
