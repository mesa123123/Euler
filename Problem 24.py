import math

def SolvePermutations(goal):
        length = 10
        arr1, arr0 = [],[]
        for i in range(0,length):
            arr0.append(i)
        while length > 0:
            totalCombinations = math.factorial(length)
            increment, place, counter = totalCombinations/length, 0,0
            while place < goal:
                place += increment
                counter += 1
            goal = goal - (place - increment)
            arr1.append(arr0[counter-1])
            del(arr0[counter-1])
            length -= 1
        return arr1

print(SolvePermutations(1000000))