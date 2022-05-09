#Python 3.9.5
#TFM_Javi
#
import json, os, serial, serial.tools.list_ports, warnings, random, multiprocessing, threading

from multiprocessing import Process, Queue

from time import time, sleep
from threading import Thread
from pydub import AudioSegment
from pydub.playback import play




#Variables de Configuración
#Determina si el sesor esta a una distancia en la que necesita una pista
def sondChooser(sensor, distancia, distancias):
    #distancias = sensor_distance[str(sensor)]
    sound = 0
    for d in distancias:
        if distancia > d["min"] and distancia < d["max"]:
            sound = d["pista"] 
    return sound

#Reproduce el Sonido
def playSoundQueue(path_sound,db):
    song = AudioSegment.from_wav(path_sound)
    song = song + db
    #song.apply_gain(volume_change)
    play(song)

#Va ejecutando los sonidos dentro de la cola cada tantos segundosg
def loopCola(cola, max_sounds,tiempoPulso, extension, song_db):
    reproduciendo = 0
    while True:
        sonidos_hilo = sum(extension in t.getName() for t in threading.enumerate())
        if len(cola) > 0 and sonidos_hilo < max_sounds:
            if sum(t.getName() == cola[0][0]  for t in threading.enumerate()) == 0:
                db = song_db[cola[0][1]]
                playtmp = Thread(target = playSoundQueue, args=(cola[0][0],db ), name=cola[0][0])
                playtmp.start()
            cola.pop(0)
        sleep(tiempoPulso) 

def deteccionPuertos():
    arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'tty' in p.name  # may need tweaking to match new arduinos
    ]
    if not arduino_ports:
        raise IOError("No Arduino found")
    if len(arduino_ports) > 1:
        warnings.warn('Multiple Arduinos found - using the first')

    return serial.Serial(arduino_ports[0])

def main():
    print("Incio tfm_javier")
    #Lectura de JSONS

    json_file = json.load(open(os.path.dirname(__file__) + "/config/conf.json", 'r'))
    sound_control_conf = json_file["sound_control"][0]
    sounds_list = json_file["sounds_list"][0]
    device_conf = json_file["device_conf"][0]
    sensor_distance = json_file["sensor_distance"][0]
    song_db = json_file["song_db"][0]
    arduino = deteccionPuertos()
    sensores ={} 
    print(serial)
   # arduino = serial.Serial(device_conf["port"] , device_conf["baudroute"] )
   #vars 
    tiempoPulso = sound_control_conf["pulso"]
    max_sounds = sound_control_conf["max_sounds"]
    extension = sounds_list["ext"]
    fin = False
    cola =[] 
    identificador = 0
    distancia = 0

    #Hilo ejecución Canciones y Lectura
    tCanciones = Thread(target = loopCola, args = (cola,max_sounds,tiempoPulso,extension, song_db))
   # tEscaneo = Thread(target = escaneoSensores, args=())

   # tFinPrograma = Thread(target = finPrograma, args = (fin,))

    #iniciar hilos
    tCanciones.start()

    #tFinPrograma.start()
    while fin == False:
        #test --> rn = ID random, distancia 
       # rn = random.randrange(1,9)
       # dr = random.randrange(0,400)
       # sensor = rn
       # distancia = dr
        #test ----- fin
       # sleep(1)
        tmp = int.from_bytes(arduino.read(), "big")
        if tmp & 0x80 == 0:
            identificador = tmp
            identificador = identificador >> 3
            sensores[str(identificador)] = (tmp & 0x0003) << 7
            print("Identificador", identificador)
        else:
            print("identificador ",identificador)
            distancia = sensores[str(identificador)] + (tmp & 0x7F)
            print("distancia ",distancia)
            sound = sondChooser(identificador, distancia, sensor_distance[str(identificador)])
            if sound > 0:         
                cancion = sounds_list["dir"]  + sounds_list[str(sound)] + extension
                elementCola = (cancion,str(sound))
                cola.append(elementCola)



if __name__ == '__main__':
    # sys.exit(main(sys.argv)) # used to give a better look to exists
    main()