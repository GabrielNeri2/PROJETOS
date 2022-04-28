def imprimir(msg):
    print()
    print('=' * 64)
    print(f'{msg:^64}')
    print('=' * 64)
    print()
#MEGA-SENA
imprimir("JOGO DA MEGA-SENA!")
from random import sample,seed
premio = sample(range(1, 61), 6)
premio = sorted(premio)
aposta = []
for i in range(1, 7):
  x = 0
  while x < 1 or x > 60 or x in aposta:
    x = int(input(f'{i}º número - Digite um número entre 1 e 60 = '))
  aposta.append(x)
aposta = sorted(aposta)
print('A sua aposta foi', aposta)
import numpy as np
sorte = np.in1d(aposta, premio)
numero = len(np.intersect1d(aposta, premio))
print('Você é um novo milionário') if sorte.all() else print(f'Não foi dessa vez, você acertou {numero} número(s).')
print('\nSorteio   ', premio)
print('Sua aposta foi ', aposta)
imprimir("JOGO DA MEGA-SENA!")
#QUINA
imprimir("JOGO DA QUINA!")
from random import sample,seed
premio = sample(range(1, 81), 5)
premio = sorted(premio)
aposta = []
for i in range(1, 6):
  x = 0
  while x < 1 or x > 80 or x in aposta:
    x = int(input(f'{i}º número - Digite um número entre 1 e 80 = '))
  aposta.append(x)
aposta = sorted(aposta)
print('A sua aposta foi', aposta)
import numpy as np
sorte = np.in1d(aposta, premio)
numero = len(np.intersect1d(aposta, premio))
print('Você é um novo milionário') if sorte.all() else print(f'Não foi dessa vez, você acertou {numero} número(s).')
print('\nSorteio   ', premio)
print('Sua aposta foi ', aposta)
imprimir("JOGO DA QUINA!")
#LOTO-FACIL
imprimir("JOGO DA LOTO-FACIL!")
from random import sample,seed
premio = sample(range(1, 26), 15)
premio = sorted(premio)
aposta = []
for i in range(1, 16):
  x = 0
  while x < 1 or x > 25 or x in aposta:
    x = int(input(f'{i}º número - Digite um número entre 1 e 25 = '))
  aposta.append(x)
aposta = sorted(aposta)
print('A sua aposta foi', aposta)
import numpy as np
sorte = np.in1d(aposta, premio)
numero = len(np.intersect1d(aposta, premio))
print('Você é um novo milionário') if sorte.all() else print(f'Não foi dessa vez, você acertou {numero} número(s).')
print('\nSorteio   ', premio)
print('Sua aposta foi ', aposta)
imprimir("JOGO DA LOTO-FACIL!")

















