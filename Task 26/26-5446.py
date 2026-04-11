with open(r'.\files\26_5446.txt') as file:
    N = int(file.readline())
    pipes = [tuple(map(int, i.split())) for i in file]

pipes = sorted(pipes, key=lambda x: (-x[0] + x[1], x[0]))
for i in pipes[:20]:
    print(*i)

last_pipe = pipes[0]
cnt = 1

for pipe in pipes:
    if last_pipe[0] - 2* last_pipe[1] - pipe[0]  >= 3:
        last_pipe = pipe
        cnt +=1

print(cnt,last_pipe[0])