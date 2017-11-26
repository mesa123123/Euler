import itertools

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

def PandigitalIdentities():
    numbers = list(range(1,10))
    sum = 0
    numbersPerms = itertools.permutations(numbers)
    for numbers in numbersPerms:
        if checkProduct(list(numbers)):
            sum += int(''.join(map(str, numbers[5:])))
    print("Sum is: " + str(sum))


PandigitalIdentities()

#correct answer is 45228