t = int(input())
for _ in range(t):
    abc = [int(x) for x in input().split()]
    a, b, c = abc[0],abc[1],abc[2]
    if a + b == c or a + c == b or b + c == a:
        print("YES")
    else:
        print("NO")
