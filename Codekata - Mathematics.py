x = int(input())
y = input()
y = y.split(" ")
y = [int(i) for i in y]

while True:
    for i in range(1,):
        n = (i**3)+(i+1)**3
        if n in y:
            print(n,y)
        else:
            print(-1)
            break