import random
cor=['verde','vermelho']
chances = [6,4]
carteira = 1000
while carteira > 500:
    sorteio = random.choices(cor, weights=chances, k=1)[0]
    sorteio = str(sorteio)
    print(f'\n Você possui {carteira}$')
    valor_apostado = input(f'\nQual valor deseja apostar? para desistir digite sair ')
    if (valor_apostado).lower() == 'sair':
        break
    cor_apostada = str(input(f'\nEm qual cor deseja apostar? Verde ou Vermelho :'))
    if sorteio == cor_apostada.lower():
            print(f'\na cor sorteada foi {sorteio}! Parabens você ganhou {valor_apostado}')
            carteira = carteira + int(valor_apostado)
    elif sorteio != cor_apostada.lower():
            print(f'\na cor sorteada foi {sorteio}! Que pena você perdeu {valor_apostado}')
            carteira = carteira - int(valor_apostado)
print(f"\nseu saldo final é de {carteira}$")



