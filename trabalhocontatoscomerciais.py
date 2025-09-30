print("Bem-vindo ao menu de contatos Andre Alvino")

lista_contatos = []
id_global = 5491035

def menu_contato(): # menu
    print("\n--- MENU PRINCIPAL ---")
    print("1) Cadastrar Contato")
    print("2) Consultar Contato")
    print("3) Remover Contato")
    print("4) Encerrar Programa")

def cadastrar_contato(id):
    nome = input("Digite o nome do contato: ")
    atividade = input("Digite a atividade do contato: ")
    telefone = input("Digite o telefone do contato: ")

    contato = { #lista dos contatos separados por categoria, id,nome,atividade e telefone
        "id": id,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }

    lista_contatos.append(contato.copy())
    print("Contato cadastrado!")

def consultar_contatos(): #menu de consulta
    while True:
        print("\n--- MENU DE CONSULTA ---")
        print("1. Consultar todos")
        print("2. Consultar por ID")
        print("3. Consultar por Atividade")
        print("4. Retornar ao menu")
        opçao = int(input("Escolha uma opção: "))

        if opçao == 1:
            for contato in lista_contatos:
                print(contato)

        elif opçao == 2:
            especifico = int(input("Digite o ID: "))
            encontrado = False
            for contato in lista_contatos:
                if contato["id"] == especifico:
                    print(contato)
                    encontrado = True
            if not encontrado:
                print("ID não encontrado.")

        elif opçao == 3:
            atividade = input("Digite a atividade: ")
            achou = False
            for contato in lista_contatos:
                if contato["atividade"].lower() == atividade.lower():
                    print(contato)
                    achou = True
            if not achou:
                print("Não existe contato com essa ativida.")

        elif opçao == 4:
            break

        else:
            print("Opção inválida")

def remover_contato(): #remoção de contatos
    while True:
        print('----Menu remover Contato----')
        idr = int(input("Digite o ID do contato para remover: "))
        achou = False
        for contato in lista_contatos:
            if contato["id"] == idr:
                lista_contatos.remove(contato)
                print("Contato removido!")
                achou = True
                break
        if achou:
            break
        else:
            print("ID inválido!")


#programa principal#
while True:
    menu_contato()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_contato(id_global)
        id_global += 1
    elif opcao == 2:
        consultar_contatos()
    elif opcao == 3:
        remover_contato()
    elif opcao == 4:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida!")
