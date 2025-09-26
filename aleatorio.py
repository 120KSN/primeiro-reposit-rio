import random

numero_aleatorio = random.randint(-1000, 1000)
executando = True
respostaj = -1
tentativaj = 0
tentativac = 0
a = -1000
b = 1001

while executando:
    if respostaj != numero_aleatorio:
        tentativaj += 1
        respostaj = int(input("Digite um número: "))
        if respostaj > numero_aleatorio:
            print("Mais pra baixo!")
        elif respostaj < numero_aleatorio:
            print("Mais pra cima!")
        elif respostaj == numero_aleatorio:
            print("Acertou!")
            executando = False
            print(f"O número era {numero_aleatorio} e o jogador acertou {respostaj}!")
            print(f"O jogador venceu em {tentativaj} tentativas!")
    
    respostac = random.randint(a, b)
    if respostac > numero_aleatorio:
        if b > respostac:
            b = respostac
    elif respostac < numero_aleatorio:
        if a < respostac:
            a = respostac
    elif respostac == numero_aleatorio:
        print(f"O número era {numero_aleatorio} e o computador acertou {respostac}!")
        print(f"O computador venceu em {tentativac} tentativas!")
        executando =  False
    tentativac += 1