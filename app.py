# pip install customtkinter

import customtkinter as ctk
from tkinter import filedialog

# Ciação das funcoes
def upload_file():
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo de áudio",
        filetypes=(
            ("Arquivos de áudio", "*.mp3 *.wav *.ogg *.flac *.aac"),
            ("Todos os arquivos", "*.*")
        )
    )
    #Verificar arquivo
    if file_path:
        file_label.configure(text=f"Arquivo selecionado: {file_path}", text_color="green")
    else:
        file_label.configure(text="Nenhum arquivo selecionado",text_color="red")


# Configuração aparencia
ctk.set_appearance_mode('dark')



# Criação da Janela principal
app = ctk.CTk()
app.title('Transcrever audio')
app.geometry('500x700')


# Criação dos Campos
    
    #Label
campo_label = ctk.CTkLabel(app,text='Selecione um arquivo de audio',font=("Arial", 20))
campo_label.pack(pady=25)
    #Entry
entryUpload = ctk.CTkButton(app, text="Upload do arquivo", command=upload_file)
entryUpload.pack(pady=10)     
    #Button

file_label = ctk.CTkLabel(app,text="")
file_label.pack()


 
# Inicia o loop da aplicação 
app.mainloop()
