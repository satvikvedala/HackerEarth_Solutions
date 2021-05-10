C = int(input())
ma = float("-inf")
for i in range(1,C):
    temp = C^i
    ma = max(ma,temp*i)
print(ma)
