AGENDA ={}


def mostrar_agenda():
    print("               Contatos                       ")
    if len(AGENDA)>0:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print()
        print("Agenda vazia")
        print()

    
def buscar_contato(contato):
    print("----------------------------------------------")
    print()
    print("Nome:", contato)
    print()
    print("Telefone:",AGENDA[contato]["telefone"])
    print()
    print("E-mail:",AGENDA[contato]["email"])
    print()
    print("Endereço:",AGENDA[contato]["endereco"])
    print("---------------------------------------------")


def ler_detalhes():
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    endereco = input ("Digite o endereço: ")
    return (telefone,email,endereco)

def incluir_editar_contato(contato,telefone,email,endereco):
    
    AGENDA[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco,
    }
    print("")
    print("Contato {} adicionado/alterado".format(contato))
    salvar()


def excluir_contato(contato):
    AGENDA.pop(contato)
    print("contato {} excluído".format(contato))
    salvar()


def exportar_contatos(nome_arquivo):
    try:
        diret = nome_arquivo
        with open(diret,"w") as arquivo:
            #arquivo.write("Nome , Telefone , E-mail , Endereço \n")
            for contato in AGENDA:
                telefone = AGENDA[contato]["telefone"]
                email = AGENDA[contato]["email"]
                endereco = AGENDA[contato]["endereco"]
                arquivo.write("{},{},{},{}\n".format(contato,telefone,email,endereco))
        print("Agenda exportada com sucesso")
    except :
        print()
        print("Ocorreu um erro ao exportar arquivo")
        print()


def importar_contatos(nome_arquivo):
    try:
        diret = nome_arquivo
        with open(diret, "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(",")

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                incluir_editar_contato(nome,telefone,email,endereco)           
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as error:
        print(error)


def salvar():
    exportar_contatos("Agenda.csv")


def carregar():
    try:
        diret = "Agenda.csv"
        with open(diret, "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(",")

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    "telefone": telefone,
                    "email": email,
                    "endereco": endereco,
                }
        print("Database Carregado com sucesso")
        print("{} Contatos Carregados".format(len(AGENDA)))
    except Exception as error:
        print(error)


#inicio
carregar()

while True: 
    try:
        opcao = int(input("""

                Menu

        0 para encerrar
        1 para mostrar todos os contatos
        2 para buscar contato
        3 para incluir contato
        4 para editar contato
        5 para excluir contato
        6 para exportar Agenda em um arquivo CSV
        7 para importar Agenda em um arquivo CSV

        Digite a opção desejada: 
        """))
    except:
        print()
        print("Só é permitido números na seleção do menu")
        print()
        continue

    if opcao == 0:
        print("Saindo do programa..")
        salvar()
        break

    elif opcao == 1:
        mostrar_agenda()

    elif opcao == 2:
        try:
            buscar_contato(input("Digite o nome do contato para verificar: "))
        except:
            print()
            print("Contato inexistente")
            print()
        
    elif opcao == 3:
        contato = input("Digite o nome: ")
        try:
            AGENDA[contato]
            print()
            print("Contato já existente")
            print()
            continue
        except:
            print("Incluindo Contato ", contato)
            telefone,email,endereco = ler_detalhes()
            incluir_editar_contato(contato,telefone,email,endereco)

    elif opcao == 4:
        contato = input("Digite o nome: ")
        try:
            AGENDA[contato]
            print("Editando Contato ",contato)
            telefone,email,endereco = ler_detalhes()
            incluir_editar_contato(contato,telefone,email,endereco)
            
        except:
            print()
            print("Contato inexistente")
            print()
            continue

    elif opcao == 5:
        try:
            contato = input("Digite o nome do contato para excluir: ")
            excluir_contato(contato)
        except:
            print()
            print("Contato inexistente")
            print()

    elif opcao == 6:
        print()
        print("Exportando contatos..")
        print()
        nome_arquivo =input("Digite o nome do arquivo a ser exportado: ")
        exportar_contatos(nome_arquivo)

    elif opcao == 7:
        print()
        nome_arquivo =input("Digite o nome do arquivo a ser importado: ")
        importar_contatos(nome_arquivo)

    else:
        print()
        print("Opção inexistente, selecione novamente ")
        print()

