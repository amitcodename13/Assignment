mx = 1000000
mk = [0]*(mx+1)
i = 2
while i*i <= mx:
    if mk[i] == 0:
        j = i*i
        while j <= mx:
            mk[j] = 1
            j += i
    i += 1

cnt = 0
ans = 2
while cnt < 10001:
    if mk[ans] == 0:
        cnt += 1
    ans += 1

print (ans-1)
    



    
