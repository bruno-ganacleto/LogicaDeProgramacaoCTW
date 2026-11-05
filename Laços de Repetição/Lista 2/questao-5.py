popA = 90
popB = 140
tempo = 0

while popB > popA:
    popA *= 1.035
    popB *= 1.01
    tempo += 1

print("Serão necessários ", tempo, " anos para que a população do país A fique maior que a do país B.")