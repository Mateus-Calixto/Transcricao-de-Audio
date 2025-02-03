
# Projeto de Transcrição de Áudio com Whisper

Este documento resume  a implementação pessoal de um projeto de transcrição de áudio usando a biblioteca Whisper da OpenAI e a interface gráfica em Python usando a biblioteca customtkinter. Abaixo estão os detalhes do projeto, as bibliotecas utilizadas, as dificuldades enfrentadas e as soluções aplicadas.

---

## **Sobre o Projeto**
O projeto consiste em transcrever arquivos de áudio para texto usando a biblioteca Whisper, desenvolvida pela OpenAI. O Whisper é um modelo de reconhecimento de fala que suporta múltiplos idiomas e oferece alta precisão na transcrição.

### **Objetivo**
- Carregar um arquivo de áudio (como `.mp3` ou `.m4a`).
- Usar o Whisper para transcrever o áudio em texto.
- Exibir o texto transcrito.

---

## **Bibliotecas Utilizadas**
Para implementar o projeto, as seguintes bibliotecas foram instaladas:

1. **Whisper**:
   - Biblioteca principal para transcrição de áudio.
   - Instalação:
     ```bash
     pip install openai-whisper
     ```

2. **PyTorch**:
   - Biblioteca de machine learning usada pelo Whisper.
   - Instalação (versão CPU, pois o projeto foi executado sem GPU):
     ```bash
     pip install torch torchaudio
     ```

3. **FFmpeg**:
   - Ferramenta necessária para processar arquivos de áudio.
   - Instalação:
     - Baixar do site oficial: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
     - Adicionar ao PATH do sistema para que o Whisper possa acessá-lo.

4. **Customtkinter**:
   - Interface gráfica moderna usando python.
   - Instalação:
     ```bash
      pip install customtkinter
     ```

---

## **Funcionalidades da interface**
   - Botão para abrir uma caixa de diálogo de seleção de arquivos.

   - Filtro para permitir apenas arquivos de áudio.

   - Exibição do caminho do arquivo selecionado.

---
## **Dificuldades Enfrentadas e Soluções**

### 1. **Aviso sobre FP16 não suportado em CPU**
   - **Problema**:
     ```
     UserWarning: FP16 is not supported on CPU; using FP32 instead
     ```
   - **Solução**:
     - O aviso é normal quando o Whisper é executado em CPU. Ele indica que o modelo está usando precisão de 32 bits (FP32) em vez de 16 bits (FP16), o que é mais lento, mas não afeta a funcionalidade.
     - Para suprimir o aviso, foi sugerido adicionar o seguinte código:
       ```python
       import warnings
       warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")
       ```

### 2. **Erro ao carregar o arquivo de áudio**
   - **Problema**:
     ```
     RuntimeError: Failed to load audio: Error opening input file Gravado.m4a
     ```
   - **Solução**:
     - Verificar se o arquivo de áudio existe no caminho especificado.
     - Usar o caminho completo do arquivo ou garantir que ele está no mesmo diretório do script.
     - Exemplo de código corrigido:
       ```python
       resposta = modelo.transcribe(r"C:\Users\mc323\Documents\Projetos-github\Transcrevendo-audio\Gravado.m4a")
       ```

### 3. **Erro de caractere de escape no caminho do arquivo**
   - **Problema**:
     ```
     SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
     ```
   - **Solução**:
     - Usar uma string raw (prefixo `r`) ou substituir as barras invertidas (`\`) por barras normais (`/`).
     - Exemplo de código corrigido:
       ```python
       resposta = modelo.transcribe(r"C:\Users\mc323\Documents\Projetos-github\Transcrevendo-audio\Gravado.m4a")
       ```

### 4. **Desempenho lento em CPU**
   - **Problema**:
     - O processamento em CPU é mais lento, especialmente para arquivos de áudio longos.
   - **Solução**:
     - Usar um modelo menor do Whisper, como `tiny` ou `base`, para melhorar o desempenho.
     - Exemplo:
       ```python
       modelo = whisper.load_model("base")
       ```

---

## **Código Final Funcional**
Aqui está o código final que resolveu os problemas e permitiu a transcrição do áudio:

```python
import whisper
import warnings

# Suprimir avisos sobre FP16 não suportado em CPU
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

# Carregar o modelo Whisper
modelo = whisper.load_model("base")

# Transcrever o arquivo de áudio
resposta = modelo.transcribe(r"C:\Users\mc323\Documents\Projetos-github\Transcrevendo-audio\Gravado.m4a")

# Exibir o texto transcrito
print(resposta['text'])
```
---
codigo final da interface + funcionalidade
```python
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
```
---
![Captura de tela 2025-02-03 122051](https://github.com/user-attachments/assets/5343a00d-00b5-49e9-8e6c-bb5fb0c49921)
---

## **Conclusão**
O projeto foi implementado com sucesso após resolver os problemas relacionados ao caminho do arquivo, instalação das bibliotecas e configuração do ambiente. O Whisper mostrou-se uma ferramenta poderosa para transcrição de áudio com boa qualidade com paucos ruidos , mesmo em ambientes sem GPU.
