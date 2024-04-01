print("Programa Expresso\n")
print("1 Cadastrar Restaurante")
print("2 Listar Restaurante")
print("3 Ativar Restaurante")
print("4 Sair\n")

opcao_digitada =int(input("Escolha uma opção:\n"))

#opcao_digitada = input

print("Voce escolheu", opcao_digitada)

if opcao_digitada==1:
    print("Voce escolheu Cadastrar Restaurante\n")
elif opcao_digitada==2:
    print("Voce esclheu Listar Restaurante\n")

elif opcao_digitada==3:
    print("Voce escolheu Ativar Restaurante")
else:
    print("Você escolheu Sair do programa")