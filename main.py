opcao = f'''
{' BANCO SANTANDER '.center(50, '*')}

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
LIMITE = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(f'Digite a opção desejada:\n {opcao}')
    #opcao = input(opcao)

    if opcao == 'd':
        print(f' Você escolheu depositar '.upper().center(80, '*'))
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += 'Depósito:'.ljust(40, '.') + f'R$ {valor:.2f}\n'
            print('Depósito realizado com sucesso!')
        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == 's':
        print(' Você escolheu sacar '.upper().center(80, '*'))
        valor = float(input('Informe o valor do saque: '))

        if saldo < valor:
            print('Operação falhou! Você não tem saldo suficiente.')
        elif valor > LIMITE:
            print('Operação falhou! O valor do saque excede o limite por vez.')
        elif numero_saques >= LIMITE_SAQUES:
            print('Operação falhou! Número máximo de saques excedido.')
        elif valor > 0:
            saldo -= valor
            extrato += 'Saque:'.ljust(43, '.') + f'R$ {valor:.2f}\n'
            numero_saques += 1
            print('Saque realizado com sucesso!')
        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == 'e':
        print(' Você escolheu extrato '.upper().center(80, '*'))
        if extrato == '':
            print('Não foram realizadas movimentações.')
        else:
            print(f'Aqui está o extrato:\n{extrato}')
    elif opcao == 'q':
        print(' Desconectando '.upper().center(80, '*'))
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')