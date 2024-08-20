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




<<<<<<< HEAD
=======
print('-'*20)

confirmacao = str(input('Confere seu pedido. Está correto? Aperte S para sim ou N para não ? ')).strip()

print('UM INSTANTE...')
sleep(2)

if confirmacao == 's' :
    print('EXCELENTE! VAMOS PROSSEGUIR.')
    endereço = str(input('Gentileza, Informe seu endereço para entrega: '))
    referencia = str(input('Algum ponto de referência? '))
    pagamento = int(input('''COMO SERÁ A FORMA DE PAGAMENTO?
[ 1 ] Dinheiro ou Pix
[ 2 ] Cartão de Débito
[ 3 ] Cartão de Crédito                      
Digite o número para escolher: '''))
if pagamento == 1:
    print('O Valor será de R$ XX,XX com 5% de desconto inclúido')


>>>>>>> 09caac161e87aca4c412b5c302997bae7e669d9b
