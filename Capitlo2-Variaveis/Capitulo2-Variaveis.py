nome=input("Digite um funcionário")
empresa=input("Digite a instituição")
qntde_funcionarios=int(input("Digite a quantidade de funcionários"))
mediaMensalidade=float(input("Digie a média da mensalidade"))
print(nome + " trabalha na empresa " + empresa)
print("possui: ", qntde_funcionarios, "funcionarios.")
print(" A média da mensalidade é de: " + str(mediaMensalidade))

print("------------Verifique os tipos de dados abaixo")
print("O tipo de dado da variavel [nome] é: ", type(nome))
print("O tipo de dado da variavel [empresa] é: ", type(empresa))
print("O tipo de dado da variavel [qntde_funcionarios] é: ",type(qntde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ",type(mediaMensalidade))