#Contendra el Reloj interno 
# Reloj = 0,6
# Contendra la cola de sonidos
# Ejecutara las canciones#

from time import time, sleep
import threading
from pydub import AudioSegment
from pydub.playback import play
#hash map
#vars
tiempoPulso = 0.6
colaReproduccion =[]

#Reproduce el Sonido

def playSoundQueue(threadName, path_sound):
    song = AudioSegment.from_wav(path_sound)
    play(song)

#Añade canciones a la cola
def addQueue(ruta_sonido,cola):
   #Si esta reproduciendo
   if threading.enumerate().count(ruta_sonido) == 0:
       print("Se añade ", ruta_sonido, " a la cola")
       cola.append(ruta_sonido)
       print("Fin addQueue")

#Va ejecutando los sonidos dentro de la cola cada tantos segundosg
def loopCola(cola):
    while True:
        sleep(tiempoPulso)
        if len(cola) > 0:
            print("cola - ", cola[0])
            threading._start_new_thread(playSoundQueue, (cola[0] ,cola[0]))
            colaReproduccion.pop(0)



    