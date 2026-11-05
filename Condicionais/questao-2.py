pesoTerra = int(input("Informe seu peso: "))
print("Escolha um planeta:\n(1) Mercúrio\n(2) Vênus\n(3) Marte\n(4) Júpiter\n(5) Saturno\n(6) Urano")
planeta = int(input())

match planeta:
    case 1:
        pesoPlaneta = pesoTerra/10*0.37
        print("Seu peso em Mercúrio seria de ", pesoPlaneta, " KG!")
    case 2:
        pesoPlaneta = pesoTerra/10*0.88
        print("Seu peso em Vênus seria de ", pesoPlaneta, " KG!")
    case 3:
        pesoPlaneta = pesoTerra/10*0.38
        print("Seu peso em Marte seria de ", pesoPlaneta, " KG!")
    case 4:
        pesoPlaneta = pesoTerra/10*2.64
        print("Seu peso em Júpiter seria de ", pesoPlaneta, " KG!")
    case 5:
        pesoPlaneta = pesoTerra/10*1.15
        print("Seu peso em Saturno seria de ", pesoPlaneta, " KG!")
    case 6:
        pesoPlaneta = pesoTerra/10*1.17
        print("Seu peso em Urano seria de ", pesoPlaneta, " KG!")