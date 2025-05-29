import customtkinter as ctk
from PIL import Image

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

    def mostrar_input(tipo):
        preparar_tela_conteudo(mostrar_frame_consulta=True)

        entry_label = ctk.CTkLabel(frame_consulta, text=f"Digite {tipo}:")
        entry_label.grid(row=0, column=0, padx=20, pady=(20, 0))

        entry = ctk.CTkEntry(frame_consulta)
        entry.grid(row=1, column=0, padx=20, pady=(10, 0))

        botoes_frame = ctk.CTkFrame(frame_consulta, fg_color="transparent")
        botoes_frame.grid(row=2, column=0, pady=(10, 0))

        botao_enviar = ctk.CTkButton(botoes_frame, text="Enviar", width=80)
        botao_enviar.pack(side="left", padx=10)

        botao_voltar = ctk.CTkButton(botoes_frame, text="Voltar", width=80, command=voltar_para_botoes)
        botao_voltar.pack(side="left", padx=10)

    def voltar_para_botoes():
        preparar_tela_conteudo(mostrar_frame_consulta=True)
        montar_botoes_consulta()

    def montar_botoes_consulta():
        botoes = [
            ("Consultar pela Chave", "a chave do voo"),
            ("Consultar Cidade Origem", "a cidade de origem"),
            ("Consultar Cidade Destino", "a cidade de destino"),
            ("Consultar Menor Escala", "menor escala")
        ]
        for i, (texto, tipo) in enumerate(botoes):
            btn = ctk.CTkButton(
                frame_consulta,
                text=texto,
                command=lambda t=tipo: mostrar_input(t)
            )
            btn.grid(row=i, column=0, padx=20, pady=(20 if i == 0 else 10, 0), sticky='ew')


    montar_botoes_consulta()

def tela_passageiros():
    preparar_tela_conteudo(mostrar_frame_consulta=True)

    label = ctk.CTkLabel(frame_consulta, text="Digite o número do voo:")
    label.grid(row=0, column=0, padx=20, pady=(20, 0))

    entry = ctk.CTkEntry(frame_consulta)
    entry.grid(row=1, column=0, padx=20, pady=(10, 0))

    botao_enviar = ctk.CTkButton(frame_consulta, text="Enviar")
    botao_enviar.grid(row=2, column=0, padx=20, pady=(10, 0))

def tela_venda_voo():
    preparar_tela_conteudo(mostrar_frame_consulta=False)

    form_venda = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
    form_venda.grid(row=0, column=0)

    campos_venda = [
        "Nome do Passageiro",
        "Número do Voo",
        "Quantidade de Passagens",
        "Forma de Pagamento"
    ]

    for i, texto in enumerate(campos_venda):
        entry = ctk.CTkEntry(form_venda, placeholder_text=texto, width=300)
        entry.grid(row=i, column=0, pady=(10, 10))

    botao_enviar = ctk.CTkButton(form_venda, text="Enviar", fg_color='green', text_color='white')
    botao_enviar.grid(row=len(campos_venda), column=0, pady=(20, 0))

def tela_cancelamento():
    preparar_tela_conteudo(mostrar_frame_consulta=True)

    label = ctk.CTkLabel(frame_consulta, text="Digite o número do voo para cancelar:")
    label.grid(row=0, column=0, padx=20, pady=(20, 0))

    entry = ctk.CTkEntry(frame_consulta)
    entry.grid(row=1, column=0, padx=20, pady=(10, 0))

    botao_enviar = ctk.CTkButton(frame_consulta, text="Enviar")
    botao_enviar.grid(row=2, column=0, padx=20, pady=(10, 0))

def tela_cadastrar_voo():
    preparar_tela_conteudo(mostrar_frame_consulta=False)

    form_frame = ctk.CTkFrame(frame_conteudo, fg_color="transparent")
    form_frame.grid(row=0, column=0)

    campos = [
        "Número do Voo",
        "Cidade de Origem",
        "Cidade de Destino",
        "Números de Escala",
        "Valor da Passagem",
        "Lugares Disponíveis"
    ]

    for i, texto in enumerate(campos):
        entry = ctk.CTkEntry(form_frame, placeholder_text=texto, width=300)
        entry.grid(row=i, column=0, pady=(10, 10))

    botao_cadastrar = ctk.CTkButton(form_frame, text='Cadastrar Voo', fg_color='green', text_color='white')
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

botao_venda_voo = ctk.CTkButton(frame_botoes, text='VENDA', hover_color='#012E69', fg_color='#003D8D', text_color='#B6B4B5', command=tela_venda_voo)
botao_venda_voo.grid(row=3, column=0, padx=50, pady=(30, 0))

botao_cancelar_voo = ctk.CTkButton(frame_botoes, text='CANCELAMENTO', hover_color='#012E69', fg_color='#003D8D', text_color='#B6B4B5', command=tela_cancelamento)
botao_cancelar_voo.grid(row=4, column=0, padx=50, pady=(30, 0))

# Inicia app
app.mainloop()
