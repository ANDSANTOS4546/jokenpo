from random import choice
from time import sleep

print('=' * 15)  # Titulo
print('JOKENPÔ'.center(15))
print('=' * 15)

replay = ''  # Variavel de repetição

# Menu jokenpô
print('Vamos jogar Jokenpô!!!')

while True:

    print('''
    PEDRA
    PAPEL
    TESOURA
    ''')

    # Escolha do Computador
    cpu_op = ['PEDRA', 'PAPEL', 'TESOURA']
    comp = choice(cpu_op)

    # Escolha do Jogador
    player = str(input('Pedra, Papel ou Tesoura? ')).upper().strip()

    # Verificação de escolhas
    print('JO')
    sleep(.5)
    print('KEN')
    sleep(.5)
    print('PÔ!')
    sleep(.5)
    print(f'\nPlayer: {player} x {comp} :Computador')

    if player == comp:  # Verificação de empate
        print('EMPATE!!!')

    # Possibilidades de vitória do Jogador
    if player == 'PEDRA' and comp == 'TESOURA':  # Com Pedra
        print('PLAYER VENCEU!')
    elif player == 'PAPEL' and comp == 'PEDRA':  # Com Papel
        print('PLAYER VENCEU!')
    elif player == 'TESOURA' and comp == 'PAPEL':  # Com Tesoura
        print('PLAYER VENCEU!')

    # Possibilidades de vitória do Computador
    if comp == 'PEDRA' and player == 'TESOURA':  # Com Pedra
        print('COMPUTADOR VENCEU!')
    elif comp == 'PAPEL' and player == 'PEDRA':  # Com Papel
        print('COMPUTADOR VENCEU!')
    elif comp == 'TESOURA' and player == 'PAPEL':  # Com Tesoura
        print('COMPUTADOR VENCEU!')

    replay = str(input('\n\nQuer jogar novamente? [S/N]: ')).strip().upper()
    
    if replay == 'N':
        break
    
