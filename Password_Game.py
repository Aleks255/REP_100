import random, os, time

print ("Remember the password and repeat!")

def gen(f):
    aZ = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D',
          'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M',
          'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V',
          'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']
    p = []
    for i in range(f):
        p.append(random.choice(aZ))
    return "".join(p)


plr = cmp = 0
rec = -1
n = 3

while plr == cmp:
    rec += 1
    print("PASSWORD:", end=" ")
    cmp = gen(n)
    print(cmp)
    time.sleep(4)
    clr = lambda: os.system('cls')
    clr()
    plr = input()
    n += 1

print("GAME OVER! Your record: ", rec)

input()
