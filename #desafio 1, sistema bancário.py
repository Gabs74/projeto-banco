#desafio 1, sistema bancário

tela_inicial = '''
________________________
Bem vindo ao banco .PY!
________________________
O que deseja realizar?

[d] Depósito
[s] Saque
[e] extrato
[f] sair
________________________
=> '''
limite_por_saque = 500
saldo = 0
extrato = ""
LIMITE_SAQUE = 3

while True:
    
    opção = input(tela_inicial)

    if opção == 'd': 
        valor = float(input("Quanto deseja depositar?"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
            print(f"seu saldo é de R${saldo:.2f}")

        else:
            print("Valor inválido")


    elif opção == 's':
        valor = float(input("quanto você deseja sacar? (limite por saque -> R$ 500,00)\n"))
        if valor > 0 and valor > saldo:
            print("Saldo insuficiente")

        elif valor > 0 and valor <= saldo and valor < limite_por_saque:

            if LIMITE_SAQUE > 0:
                saldo -= valor
                extrato += f"Saque de R$ {valor:.2f}\n"
                print("=-=" * 20)
                print(f"seu saldo é de R${saldo:.2f}")
                print("=-=" * 20)
                LIMITE_SAQUE -= 1
            else:
                print("Limite diário de saque excedido! tente novamente amanhã")

        else:
            print('''
                  ================================================
                  você ultrapassou o limite de R$500,00 por saque
                  ================================================''')
    elif opção == 'e':

        if extrato == "":
            print("sua conta bancária não possui movimentações!")
        else:
            print(f'''
=====================
!!!{extrato}!!!
_____________________
seu saldo é R${saldo}
''')
    elif opção == "f":
        print('Obrigado por utilzar o banco .PY! :)')
        break

    else:
        print('opção inexistente, tente novamente!')
            