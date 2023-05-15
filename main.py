f = open("input.in", "r")
d = {}
n = int(f.readline().strip())


islambda = False
k = False
for line in f:
    s = line.strip()
    d[s[0]] = []
    for str in s[1:].strip().split():
        d[s[0]].append(str)
        if str == "lambda":
            islambda = True
        elif len(str) == 2:
            k = str[1].isupper()
    d[s[0]].sort(key = lambda x: -len(x))

if n==0:
    if islambda:
        print("lambda")
    else:
        print("Nu exista cuvinte de lungime 0 - multimea vida")
    quit()

def printd():
    for elem in d:
        print(elem, " ".join(d[elem]))

# printd()
ok = False
L = []
cuvinte = []
def back(i, P):
    global ok
    if i == n:
        for j in range(len(d[P])-1, -1, -1):
            if len(d[P][j]) == 1:
                L.append(d[P][j])
                if k == 1:
                    cuvinte.append("".join(L))
                else:
                    cuvinte.append("".join(reversed(L)))
                ok = True
                L.pop()
            else:
                break
    else:
        for j in range(len(d[P])):
            if len(d[P][j]) == 2:
                L.append(d[P][j][not k])
                back(i+1, d[P][j][k])
                L.pop()
            elif len(d[P][j]) == 1:
                break

back(1, 'S')
if ok == False:
    print("Nu exista cuvinte de aceasta lungime")
else:
    cuvinte = [x for x in set(cuvinte)]
    cuvinte.sort()
    print(*cuvinte, sep = "\n")
f.close()