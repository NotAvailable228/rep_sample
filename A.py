x = int(input())
y = int(input())
z = int(input())
a = sorted([x,y,z], reverse = True)
n = int(input())
p = 0
for i in range(3):
    p += a[i]
    if p >= n:
        ans = i + 1
        break
print(ans)
