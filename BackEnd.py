dVoos = {}
dPassageiros = {}
aVoos_disp = []

def cadastro_voo(chave_voo, cidade_origem, cidade_destino, num_escalas,val_passagem, qnt_lugares):
        if chave_voo not in dVoos.keys():
            if qnt_lugares < 0:
                return False, "A quantidade de lugares não pode ser menor do que 0"

            aVoos_disp.append(chave_voo)

            dVoos[chave_voo] = {
            "origem": cidade_origem,
            "destino": cidade_destino,
            "escalas": num_escalas,
            "preco": val_passagem,
            "lugares": qnt_lugares,
            "passageiros": []
            }

            return True, "Voo cadastrado com sucesso!"

        else:
            return False, f"A chave {chave_voo} já existe."

def cadastro_passageiros(cpf_chave, nome_passageiro, num_telefone, voos_comprados):
    if cpf_chave not in dPassageiros.keys():
        dPassageiros[cpf_chave] = {
        "nome": nome_passageiro,
        "telefone": num_telefone,
        "voos comprados": []
        }

        mensagens = []
        for chave_voo in voos_comprados:
            if chave_voo not in dVoos:
                mensagens.append(f"Voo {chave_voo} não encontrado.")
                continue
            if chave_voo not in aVoos_disp or dVoos[chave_voo]['lugares'] <= 0:
                mensagens.append(f"Voo {chave_voo} não está disponível.")
                continue

            dPassageiros[cpf_chave]["voos comprados"].append(chave_voo)
            dVoos[chave_voo]["passageiros"].append(cpf_chave)
            dVoos[chave_voo]["lugares"] -= 1
            mensagens.append(f"Passagem para o voo {chave_voo} cadastrada com sucesso!")

            # Retira voo da lista de voos disponíveis se não tiver mais lugares
            if dVoos[chave_voo]['lugares'] <= 0 and chave_voo in aVoos_disp:
                aVoos_disp.remove(chave_voo)  

        return True, "\n".join(mensagens)
            
    else:
       return False, f"O CPF {cpf_chave} já está cadastrado."
    
def consultar_voo_por_chave(dVoos, chave_voo):
    """
    Retorna um dict com os dados completos do voo se existir, ou None se não existir.
    """
    return dVoos.get(chave_voo)

def consultar_voos_por_origem(dVoos, cidade_origem):
    """
    Retorna uma lista de tuplas (chave_voo, dados_voo) dos voos que têm a origem especificada.
    """
    return [
        (chave, dados)
        for chave, dados in dVoos.items()
        if dados["origem"].upper().strip() == cidade_origem.upper().strip()
    ]

def consultar_voos_por_destino(dVoos, cidade_destino):
    """
    Retorna uma lista de tuplas (chave_voo, dados_voo) dos voos que têm o destino especificado.
    """
    return [
        (chave, dados)
        for chave, dados in dVoos.items()
        if dados["destino"].upper().strip() == cidade_destino.upper().strip()
    ]

def consultar_voos_menor_escala(dVoos, origem, destino):
    """
    Retorna uma lista com os voos de menor número de escalas
    entre as cidades 'origem' e 'destino'.
    Cada voo da lista é um tuple (chave, dados_voo).
    Se não houver voos, retorna lista vazia.
    """
    menor = None
    voos_menores_escalas = []
    for chave, valor in dVoos.items():
        if (valor["origem"].upper().strip() == origem.upper().strip() and
            valor["destino"].upper().strip() == destino.upper().strip()):
            if menor is None or valor["escalas"] < menor:
                menor = valor["escalas"]
                voos_menores_escalas = [(chave, valor)]
            elif valor["escalas"] == menor:
                voos_menores_escalas.append((chave, valor))
    return voos_menores_escalas
  
def get_info_voo(dVoos, dPassageiros, num_voo):
    """
    Retorna as informações detalhadas de um voo, incluindo passageiros,
    sem exibir nada ou solicitar input. Para uso no backend.

    Parâmetros:
        dVoos: dict de voos, esperadamente com estrutura dVoos[num_voo]['passageiros'], etc.
        dPassageiros: dict de passageiros pelo cpf.
        num_voo: número inteiro do voo a consultar.

    Retorna:
        dict com as informações do voo e lista de passageiros.
        Se voo não existir, retorna None.
    """
    if num_voo not in dVoos:
        return None

    voo = dVoos[num_voo]
    info_voo = {
        "numero_voo": num_voo,
        "origem": voo['origem'],
        "destino": voo['destino'],
        "lugares_disponiveis": voo['lugares'],
        "total_passageiros": len(voo['passageiros']),
        "passageiros": []
    }

    for cpf in voo["passageiros"]:
        if cpf in dPassageiros:
            info_voo["passageiros"].append({
                "nome": dPassageiros[cpf]['nome'],
                "cpf": cpf,
                "telefone": dPassageiros[cpf]['telefone']
            })
        else:
            info_voo["passageiros"].append({
                "nome": None,
                "cpf": cpf,
                "telefone": None,
                "aviso": "Passageiro não encontrado no dPassageiros"
            })

    return info_voo
                        
def listar_voos_para_cancelamento(cpf, dPassageiros, dVoos):
    """
    Retorna uma lista com os voos comprados do passageiro para seleção de cancelamento.

    Parâmetros:
        cpf (int ou str): CPF do passageiro
        dPassageiros (dict)
        dVoos (dict)

    Retorno:
        (ok, lista_ou_msg):
            Se ok == False: lista_ou_msg é mensagem de erro
            Se ok == True: lista_ou_msg é lista de dicts com detalhes dos voos, cada um contendo chave 'indice' (base 1 para o usuário)
    """
    if cpf not in dPassageiros:
        return False, "CPF não encontrado."
    voos = dPassageiros[cpf].get("voos comprados", [])
    if not voos:
        return False, "Passageiro não possui voos comprados."
    lista = []
    for i, voo in enumerate(voos, start=1):
        info_voo = dVoos.get(voo, {})
        lista.append({
            "indice": i,
            "voo_codigo": voo,
            "origem": info_voo.get("origem", ""),
            "destino": info_voo.get("destino", ""),
            "escalas": info_voo.get("escalas", ""),
            "preco": info_voo.get("preco", ""),
            "lugares": info_voo.get("lugares", ""),
        })
    return True, lista

def cancelar_voo_por_indice(cpf, indice, dPassageiros, dVoos, aVoos_disp):
    """
    Cancela o voo comprado de acordo com índice informado (base 1, igual à exibição para o usuário).
    Parâmetros:
        cpf (int ou str): CPF do passageiro
        indice (int): índice do voo na lista mostrada (de 1 em diante)
        dPassageiros, dVoos, aVoos_disp: respectivas estruturas
    Retorno:
        (ok, msg): ok True se cancelado, False se erro. msg é string explicando o resultado.
    """
    if cpf not in dPassageiros:
        return False, "CPF não encontrado."
    voos = dPassageiros[cpf].get("voos comprados", [])
    if not voos:
        return False, "Passageiro não possui voos para cancelar."
    # Checagem de índice válido
    if not (1 <= indice <= len(voos)):
        return False, "Índice inválido para cancelamento. Escolha um valor de 1 a %d." % len(voos)
    # Voo a cancelar
    idx_voo = indice - 1 # Corrige base
    voo_cancelar = voos[idx_voo]
    # Realiza operação de remoção
    if cpf in dVoos[voo_cancelar]["passageiros"]:
        dVoos[voo_cancelar]["passageiros"].remove(cpf)
        dVoos[voo_cancelar]["lugares"] += 1
        dPassageiros[cpf]["voos comprados"].pop(idx_voo)
        # Remove o passageiro caso não tenha mais voos comprados
        if not dPassageiros[cpf]["voos comprados"]:
            del dPassageiros[cpf]
            return True, f"Voo {voo_cancelar} cancelado com sucesso. Passageiro {cpf} removido do sistema."
        # Garante que o voo volte para a lista de disponíveis caso tenha vaga
        if voo_cancelar not in aVoos_disp:
            aVoos_disp.append(voo_cancelar)
        return True, f"Voo {voo_cancelar} cancelado com sucesso para o passageiro {cpf}."
    else:
        return False, "Passageiro não consta como comprador deste voo."


#cadastro_voo()
#cadastro_passageiros()
#consult_voo()
#consult_menor_escala()
#listar_passageiros()
#cancel_passageiro()
