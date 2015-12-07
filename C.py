input = open('input.txt', 'r')
output = open('output.txt', 'w')
N, tapok = input.readlines()
N = int(N.rstrip())
tapok = [int(x) for x in tapok.split()]
Distance = 0
for i in range(N-1):
    if tapok[i] < 0:
        for k in range(i+1, N):
            if tapok[k] == -tapok[i] and Distance == 0:
                Distance = k - i
            elif tapok[k] == -tapok[i] and Distance > k - i:
                Distance = k - i
print(Distance, file = output)
