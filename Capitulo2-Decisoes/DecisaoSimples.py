nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
prioridade= "SIM"
if idade>=65:
    print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário!")


