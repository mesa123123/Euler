def PandigitalIdentities():
    numbers = list(range(1,10))
    result = 0
    for k in range(10,100):
        for m in range(100,1000):
            prod2 = k*m
            if len(str(prod2)) == 4:
                 identity = [int(d) for d in str(str(k)+ str(m)+ str(prod2))]
                 identity.sort()
                 if identity == numbers:
                     print(str(k) + " " + str(m) + " " + str(prod2))
                     result += prod2
    return result

print(PandigitalIdentities())

#correct answer is 45228