mx = 2000000
mk = [0]*(mx+1)
i = 2
while i*i <= mx:
    if mk[i] == 0:
        j = i*i
        while j <= mx:
            mk[j] = 1
            j += i
    i += 1
            
ans = 0
for i in range(2, 2000000):
    if mk[i] == 0:
        ans += i

print (ans)
