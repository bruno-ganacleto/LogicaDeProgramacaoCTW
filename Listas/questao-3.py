'''
3- Em uma cidade do interior, sabe-se que de janeiro a abril de 1976 (121 dias) não ocorreu 
temperatura inferior a 15o C e nem superior a 40o C. Fazer um programa py que determine: 
a) A menor temperatura ocorrida 
b) A maior temperatura ocorrida 
c) A temperatura média do período  
'''

qtd = 17
temperaturas = []
menor_temp = 40
maior_temp = 15
soma_temp = 0

print("---- Informe as temperaturas ----")
for i in range(qtd):
    temperaturas.append(float(input(f"Temperatura na semana {i+1}: ")))
    soma_temp += temperaturas[i]
    if temperaturas[i] < menor_temp:
        menor_temp = temperaturas[i]
    if temperaturas[i] > maior_temp:
        maior_temp = temperaturas[i]

media_temp = soma_temp/qtd

print(f"Menor temperatura ocorrida --> {menor_temp}°C")
print(f"Maior temperatura ocorrida --> {maior_temp}°C")
print(f"Temperatura média no periodo --> {media_temp:.2f}°C")