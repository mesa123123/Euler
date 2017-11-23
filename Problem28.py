def numberSpiralDiagonals(x):
    return 1 if x == 1 else 4*(x**2) - 6*(x-1) + (numberSpiralDiagonals(x-2))
print(numberSpiralDiagonals(1001))
