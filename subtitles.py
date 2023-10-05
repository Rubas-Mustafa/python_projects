import assemblyai as aai
aai.settings.api_key = "01d9e9a106c1456583aaf8cab5039492"
transcriber = aai.Transcriber()
transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/espn-bears.m4a")
print(transcript.text)