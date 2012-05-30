def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

ans = 1
for i in range(1, 20):
    ans = int((ans*i)/gcd(ans, i))
print (ans)
