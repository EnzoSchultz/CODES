from funcoes import limparTela, aguarde, lerInteiro

while True:
    limparTela()
    print("HackDay- Inscriçoes")
    print("(0) Sair")
    print("(1) Nova Inscrição")
    print("(2) Lista de Inscriçoes")
    opcao = input()
    if opcao == "0":
        break
    elif opcao =="1":
        print("Informe os dados abaixo para uma nova incrição")
        nome = input("Nome")
        ra = lerInteiro("RA")
        arquivo = open("bd.atitus","a")
        


        print("Dados Salvos!")


    elif opcao == "2":
        pass
    else: 
        print("Opcao Invalida")
        aguarde(2)