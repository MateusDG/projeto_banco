def mostrar_extrato():
    print(f"\nSeu saldo é de R${saldo_em_conta}")

def sacar_dinheiro(valor):
    global saldo_em_conta
    if valor > saldo_em_conta:
        print("\nSaldo insuficiente")
    else:
        saldo_em_conta -= valor
        print(f"\nFoi retirado R${valor}")

def depositar_dinheiro(valor):
    global saldo_em_conta
    saldo_em_conta += valor
    print(f"Foi depositado R${valor}")





def main():
    global saldo_em_conta
    saldo_em_conta = 1000.0
    nome = input("Digite seu nome: ")

    print(f"""
            #####################################
            Bem vindo, {nome}, ao Banco Gottardi!
            #####################################
           
           """)
    
    while True:
        opcao = int(input("""
                 [1] - Ver extrato
                 [2] - Sacar dinheiro
                 [3] - Depositar dinheiro
                 [0] - Sair do programa
                    
                 Selecione a opção: """))
        
        if opcao == 1:
            mostrar_extrato()
        
        elif opcao == 2:
            valor = int(input("\nDigite o valor que deseja sacar: "))
            sacar_dinheiro(valor)
        
        elif opcao == 3:
            valor = int(input("\nDigite o valor que irá depositar: "))
            depositar_dinheiro(valor)
        
        elif opcao == 0:
            print(f"\nObrigado por utilizar nossos serviços, {nome}.\nVolte sempre!")

main()
