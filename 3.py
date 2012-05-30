import math

n = 600851475143

range_primes = int(math.sqrt(n))

mk = [0]*(range_primes+1)

i = 2
while i*i <= range_primes:
    if(mk[i] == 0):
        j = i*i
        while j <= range_primes:
            mk[j] = 1
            j += i
    i += 1

ans = range_primes

while ans >= 2:
    if (n%ans == 0) and (mk[ans] == 0):
        break
    ans -= 1
print (ans)
