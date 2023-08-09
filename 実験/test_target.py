N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]

print(*l, sep="\n")
