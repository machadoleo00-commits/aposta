import random
cor=['verde','vermelho']
chances = [6,4]
carteira = 1000
sorteio = random.choices(cor, weights=chances, k=1)
print(f'a cor sorteada foi {sorteio}')