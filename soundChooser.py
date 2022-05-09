#serial == pip install pyserial#
# playsound == pip install playsound

# playsound is relying on another python subprocess. 
# Please use `pip install pygobject` 
# if you want playsound to run more efficiently.#
#Guardar aqui los sonidos, pasarlos a SoundControl

import serial, random
from pydub import AudioSegment
from pydub.playback import play
# Puerto del arduino
arduino_port = "/dev/ttyUSB0"
baudroute = "9600"
ids = []
#Recoge el arduino 
try:
    arduino = serial.Serial(arduino_port, baudroute)
except:
    print("Ay dios mio y el  puerto??¿?¿?¿?¿")

sensor = 0
sensores = {}
identificador = 0
listabytees =[]
#listabytees.append(arduino.read()) 

while True:
   #Cambiar a Big o Littlee 
    tmp = int.from_bytes(arduino.read(), "big")
   # listabytees.append(arduino.read()) 
    print(type(tmp))
    if tmp & 0x80 == 0:
        print("BIT DE PESO 0 ")
        identificador = tmp
        identificador = identificador >> 3
        sensores[str(identificador)] = (tmp & 0x0003) << 7
        print("Distancia PRE ? ", sensores[str(identificador)])
        print("Identificador post ", identificador)
    else:
        print("identificador post ? ",identificador)
        #sensores[str(identificador)] = bin( sensores[str(identificador)] + (tmp & 0x7F))
        aver = sensores[str(identificador)] + (tmp & 0x7F)
        print("A VER - distancia ",aver)
      #  print(" Distancia ? ",sensores[str(identificador)])
        

