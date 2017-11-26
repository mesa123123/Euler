import math


def checkProduct(numberList):
    if int(numberList[0]) == 4:
        lMultiplier = int(''.join(map(str,numberList[1:5])))
        lResult = int(''.join(map(str,numberList[5:])))
        if 4*lMultiplier == lResult:
            return True
    Mulitplicand = int(''.join(map(str, numberList[:2])))
    Multiplier = int(''.join(map(str, numberList[2:5])))
    Result = int(''.join(map(str, numberList[5:])))
    if Mulitplicand * Multiplier == Result:
        return True
    else:
        return False

def permutations(word):
        if len(word) <= 1:
            return [word]
        # get all permutations of length N-1
        perms = permutations(word[1:])
        char = word[0]
        result = []
        # iterate over all permutations of length N-1
        for perm in perms:
            # insert the character into every possible location
            for i in range(len(perm) + 1):
                result.append(perm[:i] + char + perm[i:])
        return result


def PandigitalIdentities():
    numbers = list(range(1,10))
    sum = 0
    numbersPerms = permutations(str(''.join(map(str,numbers))))
    for numbers in numbersPerms:
        if checkProduct(list(numbers)):
            sum += int(''.join(map(str, numbers[5:])))
    print("Sum is: " + str(sum))


PandigitalIdentities()

#correct answer is 45228