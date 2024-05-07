import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

li=['sagar','rohan','pranaya','nabin']
for a in li:



  speaker.Speak(f"hello mister {a}")