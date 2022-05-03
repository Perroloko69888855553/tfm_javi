#Python 3.9.5
#
import json, os

import multiprocessing
from multiprocessing import Process, Queue

from time import time, sleep
from threading import Thread
import threading
from pydub import AudioSegment
from pydub.playback import play
import random 

#Distancia
def sondChooser(sensor, distancia, sensor_distance):
    distancias = sensor_distance[str(sensor)]
    sound = 0
    for d in distancias:
        if distancia > d["min"] and distancia < d["max"]:
            sound = d["pista"] 
    return sound

#Reproduce el Sonido
def playSoundQueue(path_sound):
    song = AudioSegment.from_wav(path_sound)
    play(song)

#Va ejecutando los sonidos dentro de la cola cada tantos segundosg
def loopCola(cola, max_sounds,tiempoPulso, extension):
    print("Entra loopCola")
    reproduciendo = 0
    while True:
        sonidos_hilo = sum(extension in t.getName() for t in threading.enumerate())
        if len(cola) > 0 and sonidos_hilo < max_sounds:
            if sum(t.getName() == cola[0]  for t in threading.enumerate()) == 0:
                playtmp = Thread(target = playSoundQueue, args=(cola[0], ), name=cola[0] )
                playtmp.start()
               # print("THREADS ----------- ", threading.enumerate())
            cola.pop(0)
        sleep(tiempoPulso) 

def main():
    print("Incio tfm_javier")
    json_file = json.load(open(os.path.dirname(__file__) + "/config/conf.json", 'r'))
    sound_control_conf = json_file["sound_control"][0]
    sounds_list = json_file["sounds_list"][0]
    device_conf = json_file["device_conf"][0]
    sensor_distance = json_file["sensor_distance"][0]
   #vars 
    tiempoPulso = sound_control_conf["pulso"]
    max_sounds = sound_control_conf["max_sounds"]
    extension = sounds_list["ext"]
    cola =[] 
   #test 
    t1 = Thread(target = loopCola, args = (cola,max_sounds,tiempoPulso,extension))
    t1.start()
    while True:
        rn = random.randrange(1,9)
        distancia = random.randrange(0,400)
        sound = sondChooser(rn, distancia, sensor_distance)
        if sound > 0:
            cancion = sounds_list["dir"]  + sounds_list[sound] + extension
            print("cancion - ", cancion)
            # cola.append(cancion)
        


    
    







if __name__ == '__main__':
    # sys.exit(main(sys.argv)) # used to give a better look to exists
    main()