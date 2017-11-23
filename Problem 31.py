
def solveCoins(target):
    coins = [1,2,5,10,20,50,100,200]
    ways = [1] + [0]*target
    for coin in coins:
            for i in range(coin,target+1):
                    ways[i] += ways[i-coin]
            print(ways)
    return ways

answer = solveCoins(200)
print(answer[200])


'''
    sumTotal = 1
    for b in range(200,-1,-100):
        for c in range(b,-1,-50):
            for d in range(c,-1,-20):
                for e in range(d,-1,-10):
                    for f in range(e,-1,-5):
                        for g in range(f,-1,-2):
                            sumTotal += 1
                            print([b,c,d,e,f,g])
    return sumTotal
'''