from time import sleep

print('{:=^130}'.format('\033[1;4;31m SEJA BEM VINDO AO MARILDIZ BURGUER\033[m '))


print('POR FAVOR:')
nome = input('Digite seu nome: ')
print('Olá, {} !'.format(nome))

print('FAÇA SEU PEDIDO')

print('-'*20)



def fazer_big_mac(sand = input('Digite seu sanduiche:') ):
    print(f'Sanduíche: {sand}')

def fazer_batata(tamanho = input('Tamanho da batata : ')):
    print(f'Batata : {tamanho}')

def preparar_refri(tipo = input('Qual refri: ') , tamanho = input('Tamanho do refri: ')):
    print(f'{tipo} {tamanho}')




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


