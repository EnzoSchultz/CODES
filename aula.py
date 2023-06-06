nome = input("Nome do vendedor: ") 
salariofixo = float(input("Salario fixo: "))
valorvendas = float (input("Vendas efetuadas no mes: "))

comissao = valorvendas*0.15

total = salariofixo+comissao

print("O salario total do vendedor",nome, "vai ser de :",total)

