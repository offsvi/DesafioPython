# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# Inicio variaveis ---------
termo1 = int(0) 
termo2 = int(1)
termo3 = int(0)
print('-'*42)
print(''*3, 'Consulta de sequencia de Fibonacci')
print('42')
valor = int(input('Disgite o número: '))

# Inicio do laço de repetição 
while valor > termo3:
     termo3 = termo1 + termo2
     termo1 = termo2
     termo2 = termo3
if valor == 0 or valor == 1:
    print('O número faz parte da sequncia de fibonacci.')

elif valor == termo3:
    print('O númmero faz parte da sequência de Fibonacci.')

else:
    print('O número digitado não faz parte da sequencia de Fibonacci!')

# -------- Fim do Programa --------