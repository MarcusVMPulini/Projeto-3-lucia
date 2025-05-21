import customtkinter as ctk

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("1620x920")
app.title("CALMA AIRLINES")
app.iconbitmap("calma_airlines_logo.ico")

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=0) 
app.grid_columnconfigure(1, weight=0) 
app.grid_columnconfigure(2, weight=1) 

frame_botoes = ctk.CTkFrame(app, width=300, height=920, fg_color='yellow')
frame_botoes.grid(row=0, column=0, sticky='ns')

frame_consulta = ctk.CTkFrame(app, width=200, height=920, fg_color='gray25')
frame_consulta.grid(row=0, column=1, sticky='ns')
frame_consulta.grid_propagate(False)
frame_consulta.grid_remove()

frame_conteudo = ctk.CTkFrame(app, width=1120, height=920, fg_color='red')
frame_conteudo.grid(row=0, column=2, sticky='nsew')

frame_conteudo.grid_rowconfigure(0, weight=1)
frame_conteudo.grid_columnconfigure(0, weight=1)

painel_visivel = False
def tela_consultar_voo():
    global painel_visivel
    if painel_visivel:
        frame_consulta.grid_remove()
        painel_visivel = False
    else:
        frame_consulta.grid()
        painel_visivel = True

        for widget in frame_consulta.winfo_children():
            widget.destroy()
        label_consulta = ctk.CTkLabel(frame_consulta, text="Painel de Consulta")
        label_consulta.grid(row=0, column=0, padx=10, pady=10)

def tela_cadastrar_voo():
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

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

botao_menor_escala_voo = ctk.CTkButton(frame_botoes, text='ESCALA', hover_color='#A80101', fg_color='red', text_color='black')
botao_menor_escala_voo.grid(row=2, column=0, padx=50, pady=(30, 0))

botao_passageiros_voo = ctk.CTkButton(frame_botoes, text='PASSAGEIROS', hover_color='#A80101', fg_color='red', text_color='black')
botao_passageiros_voo.grid(row=3, column=0, padx=50, pady=(30, 0))

botao_venda_voo = ctk.CTkButton(frame_botoes, text='VENDA', hover_color='#A80101', fg_color='red', text_color='black')
botao_venda_voo.grid(row=4, column=0, padx=50, pady=(30, 0))

botao_cancelar_voo = ctk.CTkButton(frame_botoes, text='CANCELAMENTO', hover_color='#A80101', fg_color='red', text_color='black')
botao_cancelar_voo.grid(row=5, column=0, padx=50, pady=(30, 0))

app.mainloop()
