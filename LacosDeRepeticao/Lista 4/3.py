desgaste = 0; contador = 0
while desgaste < 500:
    contador += 1
    if contador > 70: desgaste += 10
    else: desgaste += 7

print(f"Ciclos completos: {contador}     Desgaste final: {desgaste}")
