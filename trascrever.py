
import whisper
import warnings

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")
modelo = whisper.load_model("medium")

resposta = modelo.transcribe("C:/Users/mc323/Documents/Projetos-github/Transcrevendo-audio/audios five/pregação-krisman-aprimorado.mp3")

print(resposta['text'])