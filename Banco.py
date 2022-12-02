import os, time

menu = """
[1] Depósito
[2] Sacar
[3] Extrato
[4] Sair

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    try:
        os.system('cls')
        print(f"Saldo = R${saldo:1.2f}")
        op = int(input(menu))

        if op == 1:
            while True:
                os.system('cls')
                print("Depósito".center(30,"#"))
                try:
                    deposito = float(input("[0] Para Cancelar\nValor do depósito: "))
                    if deposito < 0:
                        print("Use Apenas números!")
                        time.sleep(1.4)
                    elif deposito == 0:
                        break
                    else:
                        saldo += deposito
                        extrato += f"\nDepósito---- R$  {deposito:-9.2f}"
                        break
                except ValueError:
                    print('Use apenas números.')
                    time.sleep(1.4)

        elif op == 2:
            if (numero_saques >= LIMITE_SAQUE):
                os.system('cls')
                print("Saque".center(30,"#"))
                print("Você atingiu o limite de saques do dia.\nPor favor aguarde até às 00:00h de amanhã.")
                time.sleep(5)
            else:
                while True:
                    os.system('cls')
                    print("Saque".center(30,"#"))
                    try:
                        saque = float(input("[0] Para Cancelar\nValor do saque: "))
                        if saque == 0:
                            break
                        elif saque < 0:
                            print("Use apenas números!")
                            time.sleep(1.4)
                        elif saque > limite:
                            print("O limite de saque é de R$:500,00")
                            time.sleep(1.4)

                        elif saque > saldo:
                            print(f"Saldo insuficiente! Você tem {saldo}")
                            time.sleep(1.4)

                        else:
                            saldo -= saque
                            extrato += f"\nSaque------- R${-saque:-11.2f}"
                            numero_saques += 1
                            break
                            

                    except ValueError:
                        print('Use apenas números.')
                        time.sleep(1.4)

        elif op == 3:
            os.system('cls')
            print("Extrato".center(30,"#"))
            print(extrato + f"\n\nSaldo = R${saldo:1.2f}\n")
            os.system('pause')

        elif op == 4:
            break

        else:
            print("Operação inválida. Por favor selecione a operação desejada.")
            time.sleep(2.5)
    except ValueError:
        print("Operação inválida. Por favor selecione a operação desejada.")
        time.sleep(2.5)