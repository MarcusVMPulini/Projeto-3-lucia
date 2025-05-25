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
            while qnt_lugares <= 0:
                qnt_lugares = int(input("A quantidade de lugares não pode ser igual ou menor que 0 adicione um valor valido: "))

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
            "nome": nome_passageiro,
            "telefone": num_telefone,
            "voos comprados": []
            }

            qnt_passagens_comp = int(input("Insira a quantidade de passagens diferentes que o cliente comprou: "))
            qnt_compras = 1

            while qnt_compras <= qnt_passagens_comp:

                for chaves in dVoos.keys():
                    chave_voo = int(input("Insira o numero do Voo comprado: "))
                    if chaves == chave_voo:
                        break
                    else:
                        print("\n--Insira um Voo valido\n\n")
                
                if chave_voo in aVoos_disp:
                    if chave_voo in dVoos:
                        if dVoos[chave_voo]["lugares"] > 0:
                            dPassageiros[cpf_chave]["voos comprados"].append(chave_voo)
                            dVoos[chave_voo]["passageiros"].append(cpf_chave)
                            dVoos[chave_voo]["lugares"] -= 1
                            qnt_compras += 1
                            print("Passageiro cadastrado com sucesso!")
                        else:
                            print("Este Voo ja teve todos os lugares vendidos")
        
                    else:
                        print("Chave do Voo não encontrada")

            continuar = str(input("\nDeseja continuar (S/N): ")).upper()
            if continuar != "S":
                break
                
        else:
            print(f"O CPF >{cpf_chave}< não pode ser inserido pois já existe um cadastrado")

    if dVoos[chave_voo]["lugares"] <= 0:
        aVoos_disp.remove(chave_voo)

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
                        print(f"{chave.capitalize()}: {len(valor) if key == 'passageiros' else (valor.capitalize() if isinstance(valor, str) else valor)}")
                else:
                    print("Voo não encontrado!")

                retornar = str(input("Deseja voltar ao menu de consultas?\n")).upper().strip()

                if retornar != "S".strip():
                    break

            case 2:
                pesquisa_origem = str(input("Insira a cidade de origem que você deseja consultar: "))
                validacao = False
                for chave, origem in dVoos.items():
                    if origem["origem"].upper().strip() == pesquisa_origem.upper().strip():
                        print(f"\n\tVoo {chave}:")
                        validacao = True
                        for key, value in origem.items():
                            print(f"{key.capitalize()}: {len(value) if key == 'passageiros' else (value.capitalize() if isinstance(value, str) else value)}")
                                
                if not validacao:
                    print(f"Nenhum voo encontrado com origem em {pesquisa_origem}.")

                retornar = str(input("Deseja voltar ao menu de consultas?\n")).upper().strip()

                if retornar != "S".strip():
                    break

            case 3:
                pesquisa_destino = str(input("Insira a cidade de destino que você deseja consultar: "))
                validacao = False
                for chave, destino in dVoos.items():
                    if destino["destino"].upper().strip() == pesquisa_destino.upper().strip():
                        print(f"\n\tVoo {chave}")
                        validacao = True
                        for key, value in destino.items():
                            print(f"{key.capitalize()}: {len(value) if key == 'passageiros' else (value.capitalize() if isinstance(value, str) else value)}")
                
                if not validacao:
                    print(f"Nenhum voo encontrado com destino em {pesquisa_destino}.")

                retornar = str(input("Deseja voltar ao menu de consultas?\n")).upper().strip()

                if retornar != "S".strip():
                    break
                    
            case _:
                print("Por favor escolha uma opção valida")

def consult_menor_escala():
    while True:
        pesquisa_origem_escala = str(input("Insira o nome da cidade de origem: "))
        pesquisa_destino_escala = str(input("Insira o nome da cidade de destino: "))
        validacao = False
        menor = None

        voos_menores_escalas = []

        for valor in dVoos.values():
            if valor["origem"].upper().strip() == pesquisa_origem_escala.upper().strip() and valor["destino"].upper().strip() == pesquisa_destino_escala.upper().strip():
                if menor == None or valor["escalas"] < menor:
                    menor = valor["escalas"]
                    voos_menores_escalas = [valor]
                    validacao = True
                else:
                    if valor["escalas"] == menor:
                        voos_menores_escalas.append(valor)
                
        if validacao:
            print(f"Os(s) voo(s) com menor numero de escalas de {pesquisa_origem_escala.title()} até {pesquisa_destino_escala.title()}")
            for num, voo in enumerate(voos_menores_escalas, start = 1):
                print(f"\nVoo {num}")
                for key, value in voo.items():
                    print(f"{key.capitalize()}: {len(value) if key == 'passageiros' else (value.capitalize() if isinstance(value, str) else value)}")
                
            retornar = str(input("Deseja voltar ao menu de consultas?\n")).upper().strip()

            if retornar != "S".strip():
                break
        else:
            print("Não existe Voo com este percurso.")
            retornar = str(input("Deseja voltar ao menu de consultas?\n")).upper().strip()

            if retornar != "S".strip():
                    break

            
def listar_passageiros():
    while True:
        num_voo = int(input("Digite o número do voo que deseja pesquisar: "))
        for chave in dVoos.keys():
            if chave in dVoos:

                print(f"\n---Informações do Voo{num_voo}---")
                print(f"Origem: {dVoos[chave]['origem']}")
                print(f"Destino: {dVoos[chave]['destino']}")
                print(f"Lugares Disponíveis: {dVoos[chave]['lugares']}")
                print(f"Total de passageiros: {len(dVoos[chave]['passageiros'])}")
                
                if dVoos[chave]["passageiros"]:
                    print("\n--- Passageiros ---")
                    for cpf in dVoos[chave]["passageiros"]:
                        if cpf in dPassageiros:
                            print(f"Nome: {dPassageiros[cpf]['nome']}")
                            print(f"CPF:{cpf}")
                            print(f"Telefone: {dPassageiros[cpf]['telefone']}\n")
                        else:
                            print(f"CPF{cpf} não encontrado.")
                else:
                    print("Nenhum passageiro cadastrado neste voo.")
            else:
                print("Voo não encontrado")

            voltar = input("\nDeseja consultar outro voo? (S/N): ").strip().upper()
            if voltar != "S":
                break
                        
def cancel_passageiro():
    while True:
        cpf_cancelar = int(input("Insira o CPF que você deseja cancelar: "))

        if cpf_cancelar in dPassageiros.keys():
            for i, voo in enumerate(dPassageiros[cpf_cancelar]["voos comprados"], start = 1):
                if cpf_cancelar in dVoos[voo]["passageiros"]:
                    print(f"--{i}º Voo do {dPassageiros[cpf_cancelar]['nome']} com CPF {cpf_cancelar}\n")
                    print(f"""Voo: {voo}
Origem: {dVoos[voo]['origem']}
Destino: {dVoos[voo]['destino']}
Escalas: {dVoos[voo]['escalas']}
Preço: {dVoos[voo]['preco']}
Lugares: {dVoos[voo]['lugares']}
""")

            valor_cancel = int(input("Insira o valor de qual cadastro deseja cancelar: "))
            
            if 1 <= valor_cancel <= dPassageiros[cpf_cancelar]["valor comprados"]:
                dPassageiros[cpf_cancelar]["voos comprados"].pop(valor_cancel - 1)

                if cpf_cancelar in dVoos[dPassageiros[cpf_cancelar]["voos comprados"]]["passageiros"]:
                    dVoos[dPassageiros[cpf_cancelar]["voos comprados"]]["passageiros"].remove(cpf_cancelar)
                    dVoos[dPassageiros[cpf_cancelar]["voos comprados"]]["passageiros"] += 1

                    print(f"{cpf_cancelar} excluido com sucesso!")

                    if dVoos[dPassageiros[cpf_cancelar]["voos comprados"]] not in aVoos_disp:
                        aVoos_disp.append(dVoos[dPassageiros[cpf_cancelar]["voos comprados"]])

                else:
                    print(f"CPF não encontrado")

            else:
                print("--Opcão invalida")

        else:
            print("\n--CPF não encontrado\n")


cadastro_voo()
cadastro_passageiros()
#consult_voo()
#consult_menor_escala()
#listar_passageiros()
cancel_passageiro()
