from datetime import datetime

limite_saque = 500.00
saldo = 0.00
now = datetime.now()
fim_do_dia = datetime(now.year, now.month, now.day, 23, 59, 59)
total_saques_diarios = 0
sair_loop = False
extrato = []

if now > fim_do_dia:
    total_saques_diarios = 0

def deposito(valor):
    global saldo

    if valor > 0 :
        saldo += valor
        saldo = round(saldo, 2)
        print("Depósito feito")
        print(f"Saldo atual: {saldo:.2f}")
        extrato.append({"tipo": "DEPOSITO", "valor": f"{round(valor, 2):.2f}", "date": f"{datetime.now().strftime("%d/%m/%y %H:%M")}"})
    else:
        print("Deposite um valor válido")

def visualizar_extrato():
    extrato_formated = ""
    for item in extrato:
        extrato_formated += f"{item["tipo"]} {item["valor"]} R$ - {item["date"]}\n"

    print(f"""
    --------    EXTRATO    --------
{extrato_formated}
    """)

def saque(valor):
    global saldo
    global total_saques_diarios

    if not (saldo - valor < 0.0):
        if total_saques_diarios == 3:
            print("O limite de saques no dia foi atingido")
        elif limite_saque >= valor > 0.0:
            saldo -= valor
            saldo = round(saldo, 2)
            total_saques_diarios += 1
            extrato.append({"tipo": "SAQUE", "valor": f"{round(valor, 2):.2f}", "date": datetime.now().strftime("%d/%m/%y %H:%M")})
            print(f"Saldo atual: {saldo:.2f}")
        else:
            print("O limite para saque é de 500 R$")
    else:
        print("Não a limite diponível para saque")

def acoes(args):
    global sair_loop

    if args == "1":
        deposito(float(input("Insira um valor:")))
    elif args == "2":
        visualizar_extrato()
    elif args == "3":
        saque(float(input("Insira um valor:")))
    elif args == "4":
        sair_loop = True

while True:
    if sair_loop:
        break
    if datetime.now() > fim_do_dia:
        total_saques_diarios = 0
        now = datetime.now()
        fim_do_dia = datetime(now.year, now.month, now.day, 23, 59, 59)

    acoes(input("Escolha uma ação: Realizar depósito [1], Visualizar extrato [2], Realizar Saque [3], Sair [4]"))