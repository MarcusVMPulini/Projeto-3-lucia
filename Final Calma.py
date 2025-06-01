import customtkinter as ctk
from PIL import Image
import BackEnd

# Configurações iniciais
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("1620x920")
app.title("CALMA AIRLINES")
app.iconbitmap("calma_airlines_logo.ico")

# Imagens
imagem_casinha = ctk.CTkImage(light_image=Image.open("passaro.png"), size=(80, 80))
img = Image.open("Calma_aviao.png").convert("RGBA")
img.putalpha(img.getchannel("A").point(lambda p: p * 0.1))
imagem_fundo = ctk.CTkImage(img, size=(1400, 900))

# Layout
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=0)
app.grid_columnconfigure(1, weight=0)
app.grid_columnconfigure(2, weight=1)

frame_botoes = ctk.CTkFrame(app, width=300, height=920, fg_color="#002556")
frame_botoes.grid(row=0, column=0, sticky='ns')

frame_consulta = ctk.CTkFrame(app, width=200, height=920, fg_color='#003274')
frame_consulta.grid(row=0, column=1, sticky='ns')
frame_consulta.grid_propagate(False)
frame_consulta.grid_remove()

frame_conteudo = ctk.CTkFrame(app, width=1120, height=920, fg_color='#000D1E')
frame_conteudo.grid(row=0, column=2, sticky='nsew')
frame_conteudo.grid_rowconfigure(0, weight=1)
frame_conteudo.grid_columnconfigure(0, weight=1)

fundo_label = ctk.CTkLabel(frame_conteudo, image=imagem_fundo, text="")
fundo_label.place(relx=0.5, rely=0.5, anchor="center")

def preparar_tela_conteudo(mostrar_frame_consulta=True):
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

    fundo_logo = ctk.CTkLabel(frame_conteudo, image=imagem_fundo, text="")
    fundo_logo.place(relx=0.5, rely=0.5, anchor="center")

    for widget in frame_consulta.winfo_children():
        widget.destroy()

    if mostrar_frame_consulta:
        frame_consulta.grid()
    else:
        frame_consulta.grid_remove()

def tela_inicial():
    preparar_tela_conteudo(mostrar_frame_consulta=False)

def tela_consultar_voo():
    preparar_tela_conteudo(mostrar_frame_consulta=True)

    def mostrar_resultados(resultados, consulta_tipo):
        preparar_tela_conteudo(mostrar_frame_consulta=True)

        for widget in frame_consulta.winfo_children():
            widget.destroy()

        container = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
        container.pack(fill="both", expand=True, anchor = "center", padx=250, pady=10)

        label = ctk.CTkLabel(container, text=f"Resultados: {consulta_tipo}", font=("Arial", 16, "bold"))
        label.pack(pady=(10, 5))

        # Frame scrollável para os resultados
        frame_scroll = ctk.CTkScrollableFrame(container, width=580, height=300)
        frame_scroll.pack(pady=(0, 20), fill="x", expand=True)

        if not resultados:
            ctk.CTkLabel(frame_scroll, text="Nenhum voo encontrado.", text_color="#F00").pack(pady=10)
        else:
            for i, (chave, dados) in enumerate(resultados, 1):
                bloco = ctk.CTkFrame(frame_scroll, fg_color="#20253A", corner_radius=10)
                bloco.pack(fill="x", pady=7, padx=7)
                ctk.CTkLabel(
                    bloco,
                    text=f"Voo {chave} — de {dados['origem'].title()} para {dados['destino'].title()}",
                    font=("Arial", 13, "bold"),
                ).pack(anchor="w", padx=10, pady=2)
                for key, value in dados.items():
                    if key == "passageiros":
                        val_str = f"{len(value)} passageiros"
                    else:
                        val_str = value.capitalize() if isinstance(value, str) else value
                    ctk.CTkLabel(
                        bloco,
                        text=f"   {key.capitalize()}: {val_str}",
                        font=("Arial", 11)
                    ).pack(anchor="w", padx=20)

        ctk.CTkButton(container, text="Voltar", width=120, command=voltar_para_botoes).pack(pady=12)
        frame_consulta.grid_remove()

    def on_submit(tipo, *entries):
        if tipo == "a chave do voo":
            try:
                chave = int(entries[0].get())
            except Exception:
                mostrar_resultados([], "Chave inválida")
                return
            dado = BackEnd.consultar_voo_por_chave(BackEnd.dVoos, chave)
            resultados = [(chave, dado)] if dado else []
            mostrar_resultados(resultados, f"Chave {chave}")
        elif tipo == "a cidade de origem":
            origem = entries[0].get()
            lista = BackEnd.consultar_voos_por_origem(BackEnd.dVoos, origem)
            mostrar_resultados(lista, f"Origem: {origem}")
        elif tipo == "a cidade de destino":
            destino = entries[0].get()
            lista = BackEnd.consultar_voos_por_destino(BackEnd.dVoos, destino)
            mostrar_resultados(lista, f"Destino: {destino}")
        elif tipo == "menor escala":
            origem = entries[0].get()
            destino = entries[1].get()
            lista = BackEnd.consultar_voos_menor_escala(BackEnd.dVoos, origem, destino)
            mostrar_resultados(lista, f"Menor escala de {origem} para {destino}")

    def mostrar_input(tipo):
        preparar_tela_conteudo(mostrar_frame_consulta=True)
        for widget in frame_consulta.winfo_children():
            widget.destroy()

        container = ctk.CTkFrame(frame_consulta, fg_color="transparent")
        container.pack(fill="both", expand=True, anchor = "center" )
        container.place(relx=0.5, rely=0.5, anchor="center")

        if tipo == "menor escala":
            ctk.CTkLabel(container, text="Digite a cidade de origem:").grid(row=0, column=0, padx=20, pady=(20, 2), sticky="w")
            entry_origem = ctk.CTkEntry(container)
            entry_origem.grid(row=1, column=0, padx=20, pady=(2, 5))
            ctk.CTkLabel(container, text="Digite a cidade de destino:").grid(row=2, column=0, padx=20, pady=(10, 2), sticky="w")
            entry_dest = ctk.CTkEntry(container)
            entry_dest.grid(row=3, column=0, padx=20, pady=(2, 15))
            botoes_frame = ctk.CTkFrame(container, fg_color="transparent")
            botoes_frame.grid(row=4, column=0, pady=(10, 0))
            botao_enviar = ctk.CTkButton(botoes_frame, text="Voltar", width=80,
                                         command=voltar_para_botoes)
            botao_enviar.pack(side="left", padx=10)
            botao_voltar = ctk.CTkButton(botoes_frame, text="Enviar", width=80, command =lambda: on_submit(tipo, entry_origem, entry_dest))
            botao_voltar.pack(side="left", padx=10)
        else:
            ctk.CTkLabel(container, text=f"Digite {tipo}:").grid(row=0, column=0, padx=20, pady=(20, 0))
            entry = ctk.CTkEntry(container)
            entry.grid(row=1, column=0, padx=20, pady=(10, 0))
            botoes_frame = ctk.CTkFrame(container, fg_color="transparent")
            botoes_frame.grid(row=2, column=0, pady=(10, 0))
            botao_enviar = ctk.CTkButton(botoes_frame, text="Voltar", width=80, command=voltar_para_botoes)
            botao_enviar.pack(side="left", padx=10)
            botao_voltar = ctk.CTkButton(botoes_frame, text="Enviar", width=80, command=lambda: on_submit(tipo, entry))
            botao_voltar.pack(side="left", padx=10)

    def voltar_para_botoes():
        preparar_tela_conteudo(mostrar_frame_consulta=True)
        for widget in frame_consulta.winfo_children():
            widget.destroy()
        montar_botoes_consulta()

    def montar_botoes_consulta():

        container = ctk.CTkFrame(frame_consulta, fg_color="transparent")
        container.pack(fill="both", expand=True, anchor = "center" )

        frame_botoes = ctk.CTkFrame(master=frame_consulta, fg_color="transparent")
        frame_botoes.pack(fill="both", expand=True)
        frame_botoes.place(relx=0.5, rely=0.5, anchor="center")
        botoes = [
            ("Consultar pela Chave", "a chave do voo"),
            ("Consultar Cidade Origem", "a cidade de origem"),
            ("Consultar Cidade Destino", "a cidade de destino"),
            ("Consultar Menor Escala", "menor escala")
        ]
        for i, (texto, tipo) in enumerate(botoes):
            btn = ctk.CTkButton(
                master=frame_botoes,
                text=texto,
                command=lambda t=tipo: mostrar_input(t),
                width=100
            )
            btn.grid(row=i, column=0, padx=30, pady=(20 if i == 0 else 10, 0), sticky='ew')

    montar_botoes_consulta()

import customtkinter as ctk
# Supondo que os dicts e a função get_info_voo já estejam disponíveis

def tela_passageiros():
    preparar_tela_conteudo(mostrar_frame_consulta=True)

    container = ctk.CTkFrame(frame_consulta, fg_color="transparent")
    container.place(relx=0.5, rely=0.5, anchor="center")
    
    label = ctk.CTkLabel(container, text="Digite o número do voo:")
    label.pack(padx=20, pady=(20, 0))

    entry = ctk.CTkEntry(container)
    entry.pack(padx=20, pady=(10, 0))

    # Espaço reservado para o resultado, fica invisível até pesquisar
    frame_resultado = ctk.CTkScrollableFrame(frame_conteudo, width=400, height=270)
    frame_resultado.place_forget()# Inicialmente oculto

    def exibir_passageiros():
        # Limpa a área de resultado
        for widget in frame_resultado.winfo_children():
            widget.destroy()
        frame_resultado.grid_remove()

        num_voo_txt = entry.get().strip()
        try:
            num_voo = int(num_voo_txt)
        except ValueError:
            label_msg.configure(text="Número de voo inválido.")
            return

        info_voo = BackEnd.get_info_voo(BackEnd.dVoos, BackEnd.dPassageiros, num_voo)

        if not info_voo:
            label_msg.configure(text="Voo não encontrado.")
            return

        label_msg.configure(text="")  # Limpa mensagens de erro

        # INFORMAÇÕES DO VOO
        ctk.CTkLabel(frame_resultado, text=f"--- Informações do voo {info_voo['numero_voo']} ---", font=("Arial", 14, "bold")).pack(pady=(0, 5))
        ctk.CTkLabel(frame_resultado, text=f"Origem: {info_voo['origem']}").pack(anchor="w")
        ctk.CTkLabel(frame_resultado, text=f"Destino: {info_voo['destino']}").pack(anchor="w")
        ctk.CTkLabel(frame_resultado, text=f"Lugares disponíveis: {info_voo['lugares_disponiveis']}").pack(anchor="w")
        ctk.CTkLabel(frame_resultado, text=f"Total de passageiros: {info_voo['total_passageiros']}").pack(anchor="w", pady=(0, 8))

        # PASSAGEIROS DO VOO
        if info_voo["passageiros"]:
            ctk.CTkLabel(frame_resultado, text="--- Passageiros ---", font=("Arial", 11, "bold")).pack(anchor="w", pady=(2, 2))
            for p in info_voo["passageiros"]:
                nome = p.get("nome", "Desconhecido")
                cpf = p.get("cpf", "")
                telefone = p.get("telefone", "Desconhecido")
                aviso = p.get("aviso", "")

                txt_pass = f"Nome: {nome}\nCPF: {cpf}\nTelefone: {telefone}"
                if aviso:
                    txt_pass += f"\n[Atenção]: {aviso}"
                ctk.CTkLabel(frame_resultado, text=txt_pass, anchor="w", justify="left").pack(
                    anchor="w", pady=(2, 4)
                )
        else:
            ctk.CTkLabel(frame_resultado, text="Nenhum passageiro cadastrado neste voo.", text_color="orange").pack(anchor="w", pady=(5, 0))

        frame_resultado.grid()  # Exibe o frame com resultados

    botao_enviar = ctk.CTkButton(container, text="Pesquisar", command=exibir_passageiros)
    botao_enviar.pack(padx=20, pady=(10, 20))

    label_msg = ctk.CTkLabel(container, text="", text_color="red")
    label_msg.pack(padx=20, pady=(10, 0))

def tela_cadastro_e_venda():
    preparar_tela_conteudo()
    frame_consulta.grid_remove()

    frame = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    campos = ["CPF", "Nome", "Telefone"]
    entries = []
    for i, campo in enumerate(campos):
        entry = ctk.CTkEntry(frame, placeholder_text=campo, width=300)
        entry.grid(row=i, column=0, pady=(10, 10), columnspan=2)
        entries.append(entry)

    # Cria um frame scrollável para os voos!
    ctk.CTkLabel(frame, text="Selecione voos e quantidades:").grid(row=len(campos), column=0, sticky="w", pady=(10,0), columnspan=2)
    linha_inicio_voos = len(campos) + 1

    scroll_voos = ctk.CTkScrollableFrame(frame, width=320, height=240)
    scroll_voos.grid(row=linha_inicio_voos, column=0, columnspan=2, pady=(5, 10))
    # Agora o conteúdo scrollável começa!
    voos_disp = list(BackEnd.aVoos_disp)
    voo_vars = {}
    quant_entries = {}

    for idx, voo in enumerate(voos_disp):
        vagas = BackEnd.dVoos[voo]['lugares']
        var = ctk.BooleanVar()
        cb = ctk.CTkCheckBox(
            scroll_voos,
            text=f"Voo {voo} - {BackEnd.dVoos[voo]['origem']}→{BackEnd.dVoos[voo]['destino']} | Vagas: {vagas}",
            variable=var
        )
        cb.grid(row=idx, column=0, sticky="w", pady=2)
        quant = ctk.CTkEntry(scroll_voos, placeholder_text="Qtd", width=50)
        quant.grid(row=idx, column=1, padx=(10, 0))
        voo_vars[voo] = var
        quant_entries[voo] = quant

    label_msg = ctk.CTkLabel(frame, text="", text_color="white")
    label_msg.grid(row=linha_inicio_voos + 1, column=0, columnspan=2, pady=(5, 0))

    def cadastrar_e_vender_callback():
        cpf = entries[0].get().strip()
        nome = entries[1].get().strip()
        telefone = entries[2].get().strip()

        # Validação dos campos obrigatórios
        if not cpf:
            label_msg.configure(text="Preencha o CPF.", text_color="red")
            return
        if not nome:
            label_msg.configure(text="Preencha o Nome.", text_color="red")
            return
        if not telefone:
            label_msg.configure(text="Preencha o Telefone.", text_color="red")
            return
        if not cpf.isdigit():
            label_msg.configure(text="CPF inválido. Use apenas números", text_color="red")
            return
        if not telefone.isdigit():
            label_msg.configure(text="Telefone inválido. Use apenas números", text_color="red")
            return
        
        voos_a_comprar = []
        for voo in voos_disp:
            if voo_vars[voo].get():
                try:
                    qtd = int(quant_entries[voo].get())
                    if qtd < 1:
                        raise ValueError
                    vagas_disponiveis = BackEnd.dVoos[voo]['lugares']
                    if qtd > vagas_disponiveis:
                        label_msg.configure(
                            text=f"Quantidade para o voo {voo} excede o disponível ({vagas_disponiveis}).",
                            text_color="red"
                        )
                        return
                    voos_a_comprar += [voo] * qtd
                except ValueError:
                    label_msg.configure(text=f"Quantidade inválida para o voo {voo}.", text_color="red")
                    return
        if not voos_a_comprar:
            label_msg.configure(text="Selecione pelo menos um voo e quantidade.", text_color="red")
            return

        # Para passageiro cadastrado, usa backend; senão, cadastra novo
        if cpf in BackEnd.dPassageiros:
            nome = BackEnd.dPassageiros[cpf]["nome"]
            telefone = BackEnd.dPassageiros[cpf]["telefone"]
        sucesso, mensagem = BackEnd.cadastro_passageiros(cpf, nome, telefone, voos_a_comprar)
        if sucesso:
            label_msg.configure(text=mensagem, text_color="green")
            for entry in entries:
                entry.delete(0, "end")
            for ent in quant_entries.values():
                ent.delete(0, "end")
            for var in voo_vars.values():
                var.set(False)
            # Atualiza as vagas de cada voo no texto do CheckBox
            for idx, voo in enumerate(voos_disp):
                vagas = BackEnd.dVoos[voo]['lugares']
                novo_texto = f"Voo {voo} - {BackEnd.dVoos[voo]['origem']}→{BackEnd.dVoos[voo]['destino']} | Vagas: {vagas}"
                cb = scroll_voos.grid_slaves(row=idx, column=0)[0]
                cb.configure(text=novo_texto)
        else:
            label_msg.configure(text=mensagem, text_color="red")

    botao_cadastrar = ctk.CTkButton(
        frame,
        text='Cadastrar/Vender',
        fg_color='green',
        text_color='white',
        command=cadastrar_e_vender_callback
    )
    botao_cadastrar.grid(row=linha_inicio_voos + 2, column=0, pady=(20, 0), columnspan=2)

def tela_cancelamento():
    preparar_tela_conteudo(mostrar_frame_consulta=True)
    # Centraliza todo o conteúdo no frame_conteudo
    container = ctk.CTkFrame(frame_consulta, fg_color="transparent")
    container.place(relx=0.5, rely=0.5, anchor="center")

    # Label para CPF
    label_cpf = ctk.CTkLabel(container, text="Digite o CPF do passageiro:")
    label_cpf.grid(row=0, column=0, padx=20, pady=(18, 0), sticky="w")

    # Entry para CPF
    entry_cpf = ctk.CTkEntry(container)
    entry_cpf.grid(row=1, column=0, padx=20, pady=(6, 0), sticky="ew")

    # Botão para buscar voos
    botao_buscar = ctk.CTkButton(container, text="Buscar voos")
    botao_buscar.grid(row=2, column=0, padx=20, pady=(13, 0), sticky="ew")

    container_conteudo = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
    container_conteudo.place(relx=0.5, rely=0.5, anchor="center")

    # Frame para listagem dos voos com scroll
    import tkinter as tk
    frame_scroll_ext = ctk.CTkFrame(container_conteudo, fg_color="#191a20")
    frame_scroll_ext.grid(row=3, column=0, padx=20, pady=(17, 0), sticky="nsew")
    frame_scroll_ext.grid_remove()

    canvas = tk.Canvas(frame_scroll_ext, width=540, height=130, borderwidth=0, bg="#191a20", highlightthickness=0)
    scrollbar = tk.Scrollbar(frame_scroll_ext, orient="vertical", command=canvas.yview)
    frame_voos = ctk.CTkFrame(canvas, fg_color="transparent")

    frame_voos_id = canvas.create_window((0, 0), window=frame_voos, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Ajusta a largura do frame_voos ao expandir/retrair
    def on_frame_resize(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.itemconfig(frame_voos_id, width=canvas.winfo_width())

    frame_voos.bind("<Configure>", on_frame_resize)
    canvas.bind('<Configure>', on_frame_resize)

    # Label para índice do voo
    label_indice = ctk.CTkLabel(container_conteudo, text="Digite o número (índice) do voo para cancelar:")
    label_indice.grid(row=4, column=0, padx=20, pady=(17, 0), sticky="w")
    label_indice.grid_remove()

    # Entry para índice do voo
    entry_indice = ctk.CTkEntry(container_conteudo, width=60)
    entry_indice.grid(row=5, column=0, padx=20, pady=(6, 0), sticky="w")
    entry_indice.grid_remove()

    # Botão para cancelar voo
    botao_cancelar = ctk.CTkButton(container_conteudo, text="Cancelar voo")
    botao_cancelar.grid(row=6, column=0, padx=20, pady=(14, 0), sticky="w")
    botao_cancelar.grid_remove()

    # Label para mensagens/feedback
    label_msg = ctk.CTkLabel(container_conteudo, text="", text_color="white", justify="left")
    label_msg.grid(row=7, column=0, padx=20, pady=(13, 4), sticky="w")

    # Último CPF e lista de voos carregados (para não perder referência)
    ultimo_cpf = {"cpf": None, "voos": []}

    # --- CALLBACKS ---
    def buscar_voos():
        cpf = entry_cpf.get().strip()
        # Limpa frame_voos antes de popular
        for w in frame_voos.winfo_children():
            w.destroy()
        if not cpf:
            label_msg.configure(text="Digite um CPF para buscar!", text_color="red")
            frame_scroll_ext.grid_remove()
            label_indice.grid_remove()
            entry_indice.grid_remove()
            botao_cancelar.grid_remove()
            return

        ok, resultado = BackEnd.listar_voos_para_cancelamento(cpf, BackEnd.dPassageiros, BackEnd.dVoos)
        if not ok:
            label_msg.configure(text=resultado, text_color="red")
            frame_scroll_ext.grid_remove()
            label_indice.grid_remove()
            entry_indice.grid_remove()
            botao_cancelar.grid_remove()
            return

        # Popula os voos encontrados no frame_voos dinâmico
        for voo in resultado:
            info = (
                f"{voo['indice']}º - Voo: {voo['voo_codigo']} | "
                f"{voo['origem']} → {voo['destino']} | "
                f"Escalas: {voo['escalas']} | "
                f"Preço: {voo['preco']} | "
                f"Lugares: {voo['lugares']}"
            )
            l = ctk.CTkLabel(frame_voos, text=info, anchor="w", wraplength=500, justify="left", font=('Arial', 12))
            l.pack(anchor="w", pady=3, padx=2)
        frame_scroll_ext.grid()
        label_msg.configure(text="Digite o número/índice do voo e clique em 'Cancelar voo'.", text_color="white")
        label_indice.grid()
        entry_indice.grid()
        botao_cancelar.grid()
        ultimo_cpf["cpf"] = cpf
        ultimo_cpf["voos"] = resultado

    def cancelar_voo():
        cpf = ultimo_cpf["cpf"]
        if not cpf:
            label_msg.configure(text="Você precisa buscar voos primeiro.", text_color="red")
            return
        idx_txt = entry_indice.get().strip()
        if not idx_txt.isdigit():
            label_msg.configure(text="Digite um índice válido (apenas números)!", text_color="red")
            return
        idx = int(idx_txt)
        ok, resultado = BackEnd.cancelar_voo_por_indice(
            cpf,
            idx,
            BackEnd.dPassageiros,
            BackEnd.dVoos,
            BackEnd.aVoos_disp
        )
        if ok:
            label_msg.configure(text=resultado, text_color="green")
            # Atualiza lista de voos após operação
            buscar_voos()
            entry_indice.delete(0, "end")
        else:
            label_msg.configure(text=resultado, text_color="red")

    # Liga botões aos callbacks
    botao_buscar.configure(command=buscar_voos)
    botao_cancelar.configure(command=cancelar_voo)

def tela_cadastrar_voo():
    preparar_tela_conteudo()
    frame_consulta.grid_remove()

    campos = [
        "Número do Voo",
        "Cidade de Origem",
        "Cidade de Destino",
        "Números de Escala",
        "Valor da Passagem",
        "Lugares Disponíveis"
    ]
    container = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
    container.place(relx=0.5, rely=0.5, anchor="center")
    entries = []
    for i, texto in enumerate(campos):
        entry = ctk.CTkEntry(container, placeholder_text=texto, width=300)
        entry.grid(row=i, column=0, pady=(10, 10))
        entries.append(entry)
    
    label_msg = ctk.CTkLabel(container, text="", text_color="white")
    label_msg.grid(row=len(campos)+1, column=0, pady=(15, 0))

    def cadastrar_voo_callback():
        try:
            numero_voo = int(entries[0].get())
            origem = entries[1].get()
            destino = entries[2].get()
            escalas = int(entries[3].get())
            valor = float(entries[4].get())
            lugares = int(entries[5].get())
        except ValueError:
            label_msg.configure(text="Por favor, preencha todos os campos corretamente!", text_color="red")
            return
        
        sucesso, msg = BackEnd.cadastro_voo(numero_voo, origem, destino, escalas, valor, lugares)
        if sucesso:
            label_msg.configure(text=msg, text_color="green")
            for entry in entries:
                entry.delete(0, "end")
        else:
            label_msg.configure(text=msg, text_color="red")

    botao_cadastrar = ctk.CTkButton(
        container, text='Cadastrar Voo', fg_color='green', text_color='white', command=cadastrar_voo_callback
    )
    botao_cadastrar.grid(row=len(campos), column=0, pady=(20, 0))


# Botões
botao_home = ctk.CTkButton(frame_botoes, text="", image=imagem_casinha, width=40, height=40, fg_color="transparent", command=tela_inicial)
botao_home.place(x=72, y=0)

linha_divisoria = ctk.CTkFrame(frame_botoes, height=2, width=300, fg_color="gray")
linha_divisoria.place(x=0, y=85)

botao_cadastro_voo = ctk.CTkButton(frame_botoes, text='CADASTRAR', hover_color='#012E69', fg_color='#003D8D', text_color='#B6B4B5', command=tela_cadastrar_voo)
botao_cadastro_voo.grid(row=0, column=0, padx=50, pady=(330, 0))

botao_consultar_voo = ctk.CTkButton(frame_botoes, text='CONSULTAR', hover_color='#012E69', fg_color='#003D8D', text_color='#B6B4B5', command=tela_consultar_voo)
botao_consultar_voo.grid(row=1, column=0, padx=50, pady=(30, 0))

botao_passageiros_voo = ctk.CTkButton(frame_botoes, text='PASSAGEIROS', hover_color='#012E69', fg_color='#003D8D', text_color='#B6B4B5', command=tela_passageiros)
botao_passageiros_voo.grid(row=2, column=0, padx=50, pady=(30, 0))

botao_venda_voo = ctk.CTkButton(frame_botoes, text='VENDA', hover_color='#012E69', fg_color='#003D8D', text_color='#B6B4B5', command=tela_cadastro_e_venda)
botao_venda_voo.grid(row=3, column=0, padx=50, pady=(30, 0))

botao_cancelar_voo = ctk.CTkButton(frame_botoes, text='CANCELAMENTO', hover_color='#012E69', fg_color='#003D8D', text_color='#B6B4B5', command=tela_cancelamento)
botao_cancelar_voo.grid(row=4, column=0, padx=50, pady=(30, 0))

# Inicia app
app.mainloop()
