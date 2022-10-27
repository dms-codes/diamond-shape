n = 9
for i in range(1,n+1,2):
    print((i*'*').center(n))
for i in range(n-2,0,-2):
    print((i*'*').center(n))
