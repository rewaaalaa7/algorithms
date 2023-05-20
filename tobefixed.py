attraction = [0,1,2,5,6]
prices = [0,2,3,4,5]
budget = 8
cities = len(prices) 
dp = [[0 for _ in range(budget + 1 )] for _ in range(cities)]
for x in range(cities):
    for y in range(budget+1): 
        if x==0 or y ==0:
            dp[x][y] = 0
        elif prices[x] <= y:
            dp[x][y] = max(attraction[x] + dp[x -1][y-prices[x]], dp[x-1][y])
        else:
            dp[x][y] = dp[x-1][y]
            
res = dp[cities-1][y]
print(dp)
print('================')
print(res)
print('====================')
i = cities -1
j = budget
while(i>0 and j > 0):
    if dp[i][j] == dp[i-1][j]:
        print(i,' = 0')
        i -=1 
    else:
        print(i,' = 1') 
        i-=1
        j -= prices[i]
#TODO: fix printing