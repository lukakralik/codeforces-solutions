w = int(input())
k = 0
ans = ""
while(k < w):
    if w == 2:
        ans = "NO"
        break
    if w % 2 == 0 and k % 2 == 0:
        ans = "YES"
        break
    else:
        w -= 1
        k += 1
        ans = "NO"
print(ans)

