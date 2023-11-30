def solve():
    n, c, b = map(int, input().split())
    a = [-1] * n
    broq = list(map(int, input().split()))
    
    for x in broq:
        a[x - 1] = 0
 
    t = c // 2
    i = n - 2
    while i >= 0 and t:
        if a[i] == -1:
            a[i] = 1
            t -= 1
            i -= 1
        i -= 1
 
    if c % 2:
        a[0] = 1
 
    for i in range(n):
        if a[i] == -1:
            a[i] = 0
        print(a[i], end='')
 
    print()
 
if __name__ == "__main__":
    solve()



