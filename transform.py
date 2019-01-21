"""
ID: alex.go2
LANG: PYTHON3
TASK: transform
"""
f = open('comp2.txt', 'r')
g = open('output.txt', 'w')
readfile = f.readlines()
n = int(readfile[0])
arrinput = []
arroutput = []

for x in range(1, n + 1):
    arrinput.append(readfile[x][0:n])

print(arrinput)
for x in range(n + 1, 2*n + 1):
    arroutput.append(readfile[x][0:n])

print(arroutput)
