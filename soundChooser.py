#serial == pip install pyserial#
# playsound == pip install playsound

# playsound is relying on another python subprocess. 
# Please use `pip install pygobject` 
# if you want playsound to run more efficiently.#
#Guardar aqui los sonidos, pasarlos a SoundControl

import serial 
from pydub import AudioSegment
from pydub.playback import play
# Puerto del arduino
arduino_port = "/dev/ttyUSB0"
sounds =["./sounds/bonk.mp3","./sounds/toy.mp3"]
baudroute = "9600"
ids = []
#Recoge el arduino 
try:
    arduino = serial.Serial(arduino_port, baudroute)
except:
    print("Ay dios mio y el  puerto??¿?¿?¿?¿")


#Escupe todo lo que le venga del arduino#
for a in range(20):
   # print(str(arduino.readline()))
   #cm = "test"
   id = str(arduino.readline())
   cm = str(arduino.readline())
   print("ID -  ", id, " CM - ", cm)
   if id not in ids:
       ids.append(id)
  # arduino.
print(ids)
