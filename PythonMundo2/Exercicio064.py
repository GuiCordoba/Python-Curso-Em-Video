'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''
cont = soma = n = 0
while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    if n != 999:
        soma += n
    cont += 1

print(f'Você digitou {cont - 1} numeros e a soma deles é {soma}.')