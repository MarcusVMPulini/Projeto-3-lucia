import customtkinter as ctk
from PIL import Image


ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("1620x920")
app.title("CALMA AIRLINES")
app.iconbitmap("calma_airlines_logo.ico")

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=0) 
app.grid_columnconfigure(1, weight=0) 
app.grid_columnconfigure(2, weight=1) 

imagem_casinha = ctk.CTkImage(light_image=Image.open("casa.png"), size=(30, 30))
imagem_fundo = ctk.CTkImage(Image.open("Calma_aviao.png"), size=(900, 900))

frame_botoes = ctk.CTkFrame(app, width=300, height=920, fg_color='yellow')
frame_botoes.grid(row=0, column=0, sticky='ns')

def tela_inicial():
    for widget in frame_conteudo.winfo_children():
        widget.destroy()
    frame_consulta.grid_remove()
    fundo_label = ctk.CTkLabel(frame_conteudo, image=imagem_fundo, text="")
    fundo_label.place(relx=0.5, rely=0.5, anchor="center")
    global painel_visivel
    painel_visivel = False

botao_home = ctk.CTkButton(frame_botoes, text="", image=imagem_casinha, width=40, height=40, fg_color="transparent", hover_color="gray", command=tela_inicial)
botao_home.place(x=90, y=8)

linha_divisoria = ctk.CTkFrame(frame_botoes, height=2, width=300, fg_color="gray")
linha_divisoria.place(x=0, y=50)

frame_consulta = ctk.CTkFrame(app, width=200, height=920, fg_color='gray25')
frame_consulta.grid(row=0, column=1, sticky='ns')
frame_consulta.grid_propagate(False)
frame_consulta.grid_remove()


frame_conteudo = ctk.CTkFrame(app, width=1120, height=920, fg_color='red')
frame_conteudo.grid(row=0, column=2, sticky='nsew')

frame_conteudo.grid_rowconfigure(0, weight=1)
frame_conteudo.grid_columnconfigure(0, weight=1)

fundo_label = ctk.CTkLabel(frame_conteudo, image=imagem_fundo, text="")
fundo_label.place(relx=0.5, rely=0.5, anchor="center")

painel_visivel = False
def tela_consultar_voo():
    def mostrar_input(tipo):
        for widget in frame_consulta.winfo_children():
            widget.destroy()

        entry_label = ctk.CTkLabel(frame_consulta, text=f"Digite {tipo}:")
        entry_label.grid(row=0, column=0, padx=20, pady=(20, 0),  sticky='ns')

        entry = ctk.CTkEntry(frame_consulta)
        entry.grid(row=1, column=0, padx=20, pady=(10, 0),  sticky='ns')

        botao_enviar = ctk.CTkButton(frame_consulta, text="Enviar")
        botao_enviar.grid(row=2, column=0, padx=20, pady=(10, 0), sticky='ns')

    for widget in frame_conteudo.winfo_children():
        widget.destroy()

    global painel_visivel
    if painel_visivel:
        frame_consulta.grid_remove()
        painel_visivel = False
    else:
        frame_consulta.grid()
        painel_visivel = True

        for widget in frame_consulta.winfo_children():
            widget.destroy()

        botao_consultar_chave = ctk.CTkButton(frame_consulta, text="Consultar pela Chave", command=lambda: mostrar_input("a chave do voo"))
        botao_consultar_chave.grid(row=0, column=0,  padx=20, pady=(380, 0))

        botao_consultar_cidade_origem = ctk.CTkButton(frame_consulta, text="Consultar Cidade Origem", command=lambda: mostrar_input("a cidade de origem"))
        botao_consultar_cidade_origem.grid(row=1, column=0, padx=20, pady=(20, 0))

        botao_consultar_cidade_destino = ctk.CTkButton(frame_consulta, text="Consultar Cidade Destino", command=lambda: mostrar_input("a cidade de destino"))
        botao_consultar_cidade_destino.grid(row=2, column=0, padx=20, pady=(20, 0))

        botao_consultar_escala = ctk.CTkButton(frame_consulta, text="Consultar Menor escala", command=lambda: mostrar_input("menor escala"))
        botao_consultar_escala.grid(row=3, column=0, padx=20, pady=(20, 0))

def tela_passageiros():
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

    global painel_visivel
    if painel_visivel:
        frame_consulta.grid_remove()
        painel_visivel = False
    else:
        frame_consulta.grid()
        painel_visivel = True
        for widget in frame_consulta.winfo_children():
            widget.destroy()

        label = ctk.CTkLabel(frame_consulta, text="Digite o número do voo:")
        label.grid(row=0, column=0, padx=20, pady=(20, 0))

        entry = ctk.CTkEntry(frame_consulta)
        entry.grid(row=1, column=0, padx=20, pady=(10, 0))

        botao_enviar = ctk.CTkButton(frame_consulta, text="Enviar")
        botao_enviar.grid(row=2, column=0, padx=20, pady=(10, 0))


def tela_venda_voo():
    for widget in frame_conteudo.winfo_children():
        widget.destroy()
    frame_consulta.grid_remove()
    global painel_visivel
    painel_visivel = False

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
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

    global painel_visivel
    if painel_visivel:
        frame_consulta.grid_remove()
        painel_visivel = False
    else:
        frame_consulta.grid()
        painel_visivel = True
        for widget in frame_consulta.winfo_children():
            widget.destroy()

        label = ctk.CTkLabel(frame_consulta, text="Digite o número do voo para cancelar:")
        label.grid(row=0, column=0, padx=20, pady=(20, 0))

        entry = ctk.CTkEntry(frame_consulta)
        entry.grid(row=1, column=0, padx=20, pady=(10, 0))

        botao_enviar = ctk.CTkButton(frame_consulta, text="Enviar")
        botao_enviar.grid(row=2, column=0, padx=20, pady=(10, 0))


def tela_cadastrar_voo():
    for widget in frame_conteudo.winfo_children():
        widget.destroy()
        frame_consulta.grid_remove()
    frame_consulta.grid_remove()

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

botao_cadastro_voo = ctk.CTkButton(frame_botoes, text='CADASTRAR', hover_color='#A80101', fg_color='red', text_color='black', command=tela_cadastrar_voo)
botao_cadastro_voo.grid(row=0, column=0, padx=50, pady=(280, 0))

botao_consultar_voo = ctk.CTkButton(frame_botoes, text='CONSULTAR', hover_color='#A80101', fg_color='red', text_color='black', command=tela_consultar_voo)
botao_consultar_voo.grid(row=1, column=0, padx=50, pady=(30, 0))

botao_passageiros_voo = ctk.CTkButton(frame_botoes, text='PASSAGEIROS', hover_color='#A80101', fg_color='red', text_color='black', command=tela_passageiros)
botao_passageiros_voo.grid(row=3, column=0, padx=50, pady=(30, 0))

botao_venda_voo = ctk.CTkButton(frame_botoes, text='VENDA', hover_color='#A80101', fg_color='red', text_color='black', command=tela_venda_voo)
botao_venda_voo.grid(row=4, column=0, padx=50, pady=(30, 0))

botao_cancelar_voo = ctk.CTkButton(frame_botoes, text='CANCELAMENTO', hover_color='#A80101', fg_color='red', text_color='black', command=tela_cancelamento)
botao_cancelar_voo.grid(row=5, column=0, padx=50, pady=(30, 0))

app.mainloop()
