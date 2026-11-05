popA = int(input("Informe a população do país A: "))
popB = int(input("Informe a população do país B: "))

tempo = 0
while popA < popB:
    popA *= 1.03
    popB *= 1.015
    tempo += 1
    
    if tempo%5 == 0:
        popA *= 0.93
        popB *= 0.93

print(f"Irão demorar {tempo} anos para que a população do país A ultrapasse a do país B")