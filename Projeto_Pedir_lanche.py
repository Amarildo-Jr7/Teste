from time import sleep

print('POR FAVOR:')
nome = input('Digite seu nome: ')
print('Olá, {} !'.format(nome))

print('FAÇA SEU PEDIDO')

print('-'*20)

sandwich = str('Nome do sanduíche: ')
batata = str('Tamanho da bata: [P/M/G] ')
refrigerante = str('Qual refrigerante: ')
print(f'Confira por favor seu pedido:{sandwich} ,{batata}, {refrigerante}')
confir = str(input('O pedido está correto: [S/N]')).upper().strip




