ans = 0

a = 1
while a < 1000:
    b = 1
    while (a + b) < 1000:
        if (1000-a-b)*(1000-a-b) == (a*a + b*b):
            ans = a*b*(1000-a-b)
        b += 1
    a += 1
print (ans)
