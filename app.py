# pip install customtkinter

import customtkinter as ctk
from tkinter import filedialog
import os  # Importar a biblioteca os para manipulação de caminhos

#import para tradução
import whisper
import warnings


# Ciação das funcoes
def upload_file():
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo de áudio",
        filetypes=(
            ("Arquivos de áudio", "*.mp3 *.m4a *.wav *.ogg *.flac *.aac"),
            ("Todos os arquivos", "*.*")
        )
    )
    #Verificar arquivo
    if file_path:
        nome_arquivo=  os.path.basename(file_path)
        file_label.configure(text=f"Arquivo selecionado: {nome_arquivo}", text_color="green")

        #add frame 
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")
        
        modelo = whisper.load_model("base")

        resposta = modelo.transcribe(f"{file_path}")

        txt_audio = resposta['text']

        texto_audio.configure(text=txt_audio)

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
campo_label = ctk.CTkLabel(app,text='Selecione um arquivo de audio:',font=("Arial", 20))
campo_label.pack(pady=25)
    #Entry
entryUpload = ctk.CTkButton(app, text="Upload do arquivo", command=upload_file,width=150,height=40, font=("Arial", 17))
entryUpload.pack(pady=10)     
    #Button

file_label = ctk.CTkLabel(app,text="")
file_label.pack()


frame = ctk.CTkFrame(app, width=500)

texto_audio = ctk.CTkLabel(frame, text="",wraplength=400)
texto_audio.pack(pady=10, padx=10)


 
# Inicia o loop da aplicação 
app.mainloop()
