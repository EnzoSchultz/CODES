import os
import time
os.system("cls")
print("Seja bem vindo ao Sistema")
time.sleep(1)
while True:
    os.system("cls")
    print("(0) sair")
    print("(1) conversão em C")
    print("(2) conversão em F")
    opcao = input()
    if opcao == "0":
        break
    elif opcao =="1":
        print("Convertendo F para C")
        input("press enter to enter")
    elif opcao == "2":
        print("convertendo C para F")
        input("press enter to enter")
    else:
        print("Opcao Invalida!")
        input("press enter to enter")
print ("Volte sempre") 