ans = 0
for i in range(100, 999):
    for j in range(100, 999):
        n = i*j
        if(int(str(n)[::-1]) == n):
            if(n > ans):
                ans = n

print (ans)

            

       
