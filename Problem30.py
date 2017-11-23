def sumFifthPowers(x):
   return([x**5 for x in [int(dx) for dx in str(x)]])


def sumAllFifthPowers():
    set9s = [9]
    while int(''.join(map(str,set9s))) <= ((9**5)*len(set9s)):
        set9s.append(9)
    limitCase = int(''.join(map(str, set9s)))
    numbersThatEqualTheSumOfTheirFifthPowers = [i for i in range(2,limitCase) if i == sum(sumFifthPowers(i))]
    return (numbersThatEqualTheSumOfTheirFifthPowers)


print(sum(sumAllFifthPowers()))