import customtkinter as ctk


def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    # implementa validação conforme desejar
    if usuario == 'baiano' and senha == '123456':
        mensagem.configure(text='Login feito com sucesso.', text_color='green')
        return

    mensagem.configure(text='Usuário e/ou senha inválido.', text_color='red')


ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

label_usuario = ctk.CTkLabel(app, text='Usuário')
label_usuario.pack(pady=5)

campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=5)

label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=5)

campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=5)

botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=5)

mensagem = ctk.CTkLabel(app, text='')
mensagem.pack(pady=5)

app.mainloop()
