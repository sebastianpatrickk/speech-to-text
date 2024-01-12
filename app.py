import whisper

model = whisper.load_model("base")
print(model)
result = model.transcribe("original-voiceover.wav")