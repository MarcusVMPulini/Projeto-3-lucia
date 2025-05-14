dVoos = {}
dPassageiros = {}
aVoos_disp = []

def cadastro_voo():
    while True:
        chave_voo = int(input("Insira o numero do Voo: "))

        if chave_voo not in dVoos.keys():
            cidade_origem = str(input("Insira a cidade de origem: "))
            cidade_destino = str(input("Insira a cidade de destino: "))
            num_escalas = int(input("Insira o numero de escalas (paradas até o destino final): "))
            val_passagem = float(input("Insira o preço da passagem: "))
            qnt_lugares = int(input("Insira a quantidade de lugares disponiveis no voo: "))

            aVoos_disp.append(chave_voo)

            dVoos[chave_voo] = {
            "origem": cidade_origem,
            "destino": cidade_destino,
            "escalas": num_escalas,
            "preco": val_passagem,
            "lugares": qnt_lugares,
            "passageiros": []
            }

            continuar = str(input("\nDeseja continuar (S/N): ")).upper()
            if continuar != "S":
                break

        else:
            print(f"A chave >{chave_voo}< não pode ser inserida pois já existe uma cadastrado")

def cadastro_passageiros():
    while True:
        cpf_chave = int(input("Insira o CPF para cadastro: "))
        if cpf_chave not in dPassageiros.keys():
            nome_passageiro = str(input("Insira o nome do passageiro: "))
            num_telefone = int(input("Digite o numero de telefone: "))

            dPassageiros[cpf_chave] = {
            "Nome": nome_passageiro,
            "Telefone": num_telefone,
            "Voos comprados": []
            }

            continuar = str(input("\nDeseja continuar (S/N): ")).upper()
            if continuar != "S":
                break
                
        else:
            print(f"O CPF >{cpf_chave}< não pode ser inserido pois já existe um cadastrado")
            cadastro_passageiros()

    return dPassageiros

def consult_voo():
    while True:
        print(f"[ 1 ]. Consultar Voo pela chave\n[ 2 ]. Consultar Voo pela cidade de origem\n[ 3 ]. Consultar Voo pela cidade de destino\n")
        consulta = int(input(" "))
        match consulta:
            case 1:
                pesquisa = int(input("Insira a chave do Voo que você deseja consultar: "))
                if pesquisa in dVoos:
                    print(f"\nVoo {pesquisa} encontrado:")
                    for chave, valor in dVoos[pesquisa].items():
                        print(f"{chave.capitalize()}: {valor.capitalize() if isinstance(valor, str) else valor}")
                else:
                    print("Voo não encontrado!")

                retornar = str(input("Deseja voltar ao menu de consultas?\n")).upper()

                if retornar != "S":
                    break

            case 2:
                pesquisa_origem = str(input("Insira a cidade de origem que você deseja consultar: "))
                validacao = False
                for chave, origem in dVoos.items():
                    if origem["origem"].upper() == pesquisa_origem.upper():
                        print(f"\n\tVoo {chave}:")
                        validacao = True
                        for key, value in origem.items():
                            print(f"{key.capitalize()}: {len(value) if key == 'passageiros' else (value.capitalize() if isinstance(value, str) else value)}")
                                
                if not validacao:
                    print(f"Nenhum voo encontrado com origem em {pesquisa_origem}.")

                retornar = str(input("Deseja voltar ao menu de consultas?\n")).upper()

                if retornar != "S":
                    break

            case 3:
                pesquisa_destino = str(input("Insira a cidade de destino que você deseja consultar: "))
                validacao = False
                for chave, destino in dVoos.items():
                    if destino["destino"].upper() == pesquisa_destino.upper():
                        print(f"\n\tVoo {chave}")
                        validacao = True
                        for key, value in destino.items():
                            print(f"{key.capitalize()}: {len(value) if key == 'passageiros' else (value.capitalize() if isinstance(value, str) else value)}")
                
                if not validacao:
                    print(f"Nenhum voo encontrado com destino em {pesquisa_destino}.")

                retornar = str(input("Deseja voltar ao menu de consultas?\n")).upper()

                if retornar != "S":
                    break
                    
            case _:
                print("Por favor escolha uma opção valida")

cadastro_voo()
#cadastro_passageiros()
consult_voo()
