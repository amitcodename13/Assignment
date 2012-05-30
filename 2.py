ans = 0

prev2 = -1
prev1 = -1
cur = 1 

while cur <= 4000000:
    if(cur % 2 == 0):
      ans += cur
    prev2 = prev1
    prev1 = cur
    cur = prev1 + prev2

print (ans)
