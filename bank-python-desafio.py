# Sistema Bancário com Python
# Projeto de um sistema bancário com python TRILHA POTÊNCIA TECH CIÊNCIA DE DADOS COM PYTHON - DIO-ME

menu = '''
-----------------------------------------------
Bem vindo ao Banco Python!
===============================================
Escolha uma das opções abaixo para prosseguir:
-----------------------------------------------
[a] Depositar
[b] Sacar
[c] Extrato
[d] Encerrar sessão

Qual a opção desejada?
'''

# Variáveis para controle do banco
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':

        print("Sua sessão foi finalizada!")
        break

    elif opcao == 'a':
        # Depositar
        deposito = float(input("Informe o valor que será depositado: "))

        if deposito > 0:
            saldo += deposito
            mensagem = f'Depósito de R$ {deposito:.2f} realizado.\n'
            extrato += mensagem
            print(mensagem)
        else:
            print("Não é permitido depositar valores negativos.")

    elif opcao == 'b':
        # Sacar
        if numero_saques < LIMITE_SAQUES:
            saque = float(input("Informe o valor sacado: "))
            if saque > 0:
                if saque <= limite:
                    if saldo >= saque:
                        saldo -= saque
                        numero_saques += 1
                        mensagem = f'Saque de R$ {saque:.2f} realizado.\n'
                        extrato += mensagem
                        print(mensagem)
                    else:
                        print("Saldo de conta insuficiente para este saque.")
                else:
                    print(f"Valor limite de saque excedido. O limite é R$ {limite:.2f}")
            else:
                print('Não serão, permitidos saques de valores negativos.')
        else:
            print("Limite de saques excedido. Tente novamente mais tarde.")

    elif opcao == 'c':
        # Gerar extrato
        print("=====================EXTRATO======================")

        print("\nBank Python\nExtrato da conta axzsa\n")
        if extrato == '':
            print("Não foram realizadas novas movimentações.")
        else:
            print(extrato)
            print(f"O saldo da conta é R$ {saldo:.2f}")
            print("==============================================")

    else:
        print("\nOperação inválida, por favor informe novamente sua opção desejada.")
        print("\nOBRIGADO POR USAR NOSSO SISTEMA BANCÁRIO. ")
