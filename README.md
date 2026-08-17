# 🎲 Simulador de Apostas (Verde ou Vermelho)

Um jogo de apostas simples via linha de comando, desenvolvido em Python. O jogador começa com uma carteira fixa e aposta valores tentando acertar a cor sorteada, até zerar o saldo, atingir o limite mínimo ou decidir parar.

## Como funciona

- O jogador começa com **1000$** na carteira.
- A cada rodada, o programa sorteia uma cor (`verde` ou `vermelho`) com pesos diferentes — o vermelho tem mais chance de sair que o verde.
- O jogador escolhe um valor para apostar e uma cor.
- Se acertar, o valor apostado é somado à carteira. Se errar, é subtraído.
- O jogo continua enquanto a carteira estiver **acima de 500$**, ou até o jogador digitar `sair`.
- No final, o saldo restante é exibido.

## Tecnologias e conceitos aplicados

- Python 3
- Módulo `random` (`random.choices` com pesos)
- Loop `while` com condição de saída
- Estruturas condicionais (`if`/`elif`)
- Conversão de tipos (`str`, `int`)
- Entrada e saída de dados (`input`, `print`)

## Como executar

Pré-requisito: Python 3 instalado.

```bash
python nome_do_arquivo.py
```

## Possíveis melhorias futuras

- Validação de entrada (evitar erro se o jogador digitar um valor não numérico ou uma cor inválida)
- Impedir apostas maiores que o saldo disponível
- Histórico de rodadas (quantas vitórias/derrotas)
- Ajuste configurável do saldo inicial e do limite mínimo de saída
