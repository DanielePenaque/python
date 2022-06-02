#Autor:Daniele Penaque
#Data:19/05/2022

import os
os.system('cls')

#Entrada de dados
valor = float(input('Digite um valor com casas decimais: '))

print('='*50)
print('Pratica: Verificando valor quebrado')
print('-'*50)

#condicionmal
if(valor %2 ==0):
    print(f'o valor {valor} é inválido! O número digitando é inteiro')
else:
    print()
    print(f'O valor digitando foi {valor}, entrada correta!')

print('-'*50)
print('Fim do programa!')
print('-'*50)
