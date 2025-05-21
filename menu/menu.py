import customtkinter as ctk

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("1620x920")
app.title("CALMA PY")
app.iconbitmap("614.ico")

frame_botoes = ctk.CTkFrame(app, width=300, height=920, fg_color='blue')
frame_botoes.grid(column=0, sticky='nsew')

frame_conteudo = ctk.CTkFrame(app, width=1380, height=920, fg_color='red')
frame_conteudo.grid(row=0, column=1, sticky='nsew')

def tela_cadastrar_voo():
    input_numero_voo = ctk.CTkEntry(frame_conteudo, placeholder_text='Insira o numero do Voo')
    input_numero_voo.grid(row=0, column=0, pady=(600,700), padx=(480,480))

botao_cadastro_voo = ctk.CTkButton(frame_botoes, text='CADASTRAR', hover_color='#A80101', fg_color='red', text_color='black', command=tela_cadastrar_voo)
botao_cadastro_voo.grid(row=0, column=0, padx=(50,50), pady=(280,0))

botao_consultar_voo = ctk.CTkButton(frame_botoes, text='CONSULTAR', hover_color='#A80101', fg_color='red', text_color='black')
botao_consultar_voo.grid(row=1, column=0, padx=(50,50), pady=(30,0))

botao_menor_escala_voo = ctk.CTkButton(frame_botoes, text='ESCALA', hover_color='#A80101', fg_color='red', text_color='black')
botao_menor_escala_voo.grid(row=2, column=0, padx=(50,50), pady=(30,0))

botao_passageiros_voo = ctk.CTkButton(frame_botoes, text='PASSAGEIROS', hover_color='#A80101', fg_color='red', text_color='black')
botao_passageiros_voo.grid(row=3, column=0, padx=(50,50), pady=(30,0))

botao_venda_voo = ctk.CTkButton(frame_botoes, text='VENDA', hover_color='#A80101', fg_color='red', text_color='black')
botao_venda_voo.grid(row=4, column=0, padx=(50,50), pady=(30,0))

botao_cancelar_voo = ctk.CTkButton(frame_botoes, text='CANCELAMENTO', hover_color='#A80101', fg_color='red', text_color='black')
botao_cancelar_voo.grid(row=5, column=0, padx=(50,50), pady=(30,0))

app.mainloop()