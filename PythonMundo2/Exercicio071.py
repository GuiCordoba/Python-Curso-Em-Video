'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
 e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('=' * 40)
print('{:^40}'.format('BEM VINDO AO BANCO CEV'))
print('=' * 40)
total = int(input('Qual valor você deseja sacar? R$'))
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Serão {total_ced} células de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
             break
print('=' * 40)
print('Volte sempre ao banco CEV. Tenha um bom dia!')