
import win32com.client


speaker = win32com.client.Dispatch("SAPI.SpVoice")

l=['Ajay','Harsh',"Het",'Hardik','Vidit']

for i in l:
    z=f'Hello {i}'
    speaker.Speak(z)

