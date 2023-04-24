from termcolor import colored
from dicionario import acervo
import os
import random

idRandomico = random.choice(acervo)

PALAVRA = idRandomico
podeTentar = True
tentativas = 6
venceu = False
chutes = []

while(podeTentar and tentativas > 0):
    chute = input()

    chuteTemp = ''
    chuteTemp2 = ''
    os.system('cls' if os.name == 'nt' else 'clear')
    for i,letra in enumerate(chute):
        chuteTemp2 += letra
        if letra == PALAVRA[i]:
            chuteTemp += colored(letra, "green")
        elif letra in PALAVRA:
            if colored(letra, "yellow") not in chuteTemp:
                chuteTemp += colored(letra, "yellow")
            else:
                chuteTemp += letra
        else:
            chuteTemp += letra
    chutes.append(chuteTemp)
    for temp in chutes:
        print(temp)

    if chuteTemp2 == PALAVRA:
        podeTentar = False
        venceu = True
    else:
        tentativas -= 1


print('')
print(f'A palavra era {PALAVRA}')
print('')

if venceu:
    print('venceu')
else:
    print('perdeu')
