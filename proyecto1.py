
"""import timeo
import multiprocessing

# Función que se ejecuta en el proceso
def proceso(event):
    while True:
        if event.is_set():  # Si el evento está configurado, el proceso está en pausa
            print("Proceso pausado")
            time.sleep(1)
        else:  # Si el evento no está configurado, el proceso está en ejecución
            print("Proceso en ejecución")
            time.sleep(1)

if __name__ == '__main__':
    # Crear un objeto Event para indicar cuándo el proceso debe pausarse
    pausa_event = multiprocessing.Event()
    
    # Crear un objeto de proceso y pasarle el objeto Event
    p = multiprocessing.Process(target=proceso, args=(pausa_event,))
    
    # Iniciar el proceso
    p.start()
    
    # Esperar 5 segundos
    time.sleep(5)
    
    # Pausar el proceso
    print("Pausando el proceso...")
    pausa_event.set()
    
    # Esperar 5 segundos
    time.sleep(5)
    
    # Reanudar el proceso
    print("Reanudando el proceso...")
    pausa_event.clear()
    
    # Esperar a que el proceso termine
    p.join()"""

"""import time

import threading

class Contador:
    def __init__(self, id):
        self.id = id
        self.count = 0
        self.paused = False
        self.pause_cond = threading.Condition(threading.Lock())
    
    def start(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.start()
    
    def run(self):
        while True:
            with self.pause_cond:
                while self.paused:
                    self.pause_cond.wait()
                self.count += 1
                print(f"Contador {self.id}: {self.count}")
            time.sleep(1)
    
    def pause(self):
        self.paused = True
    
    def resume(self):
        with self.pause_cond:
            self.paused = False
            self.pause_cond.notify()
    
    def wait_key(self):
        while True:
            key = input()
            if key == '1':
                self.paused = not self.paused
            elif key == '2':
                self.paused = not self.paused

# Crea dos contadores
contador1 = Contador(1)
contador2 = Contador(2)

# Inicia los contadores en hilos separados
contador1.start()
contador2.start()

# Espera a que el usuario ingrese los números 1 y 2
while True:
    key = input()
    if key == '1':
        contador1.pause()
    elif key == '2':
        contador2.pause()
    elif key == '11':
        contador1.resume()
    elif key == '22':
        contador2.resume()"""

import time
import threading

class Contador:
    def __init__(self, id, posicion):
        self.id = id
        self.count = 0
        self.paused = False
        self.pause_cond = threading.Condition(threading.Lock())
        self.posicion = posicion


        
    
    def start(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    
    def run(self):
        while True:
            with self.pause_cond:
                while self.paused:
                    self.pause_cond.wait()
                self.count += 1
                print(f"\033[{self.posicion}GContador {self.id}: {self.count}")
                time.sleep(2)

    
    def pause(self):
        self.paused = True
    
    def resume(self):
        with self.pause_cond:
            self.paused = False
            self.pause_cond.notify()

            
    
    def wait_key(self):
        while True:
            key = input()
            if key == '1':
                self.paused = not self.paused
            elif key == '2':
                self.paused = not self.paused


# Crea dos contadores
contador1 = Contador(1, 1)
contador2 = Contador(2, 20)

# Inicia los contadores en hilos separados
contador1.start()
contador2.start()

# Espera a que el usuario ingrese los números 1 y 2
while True:
    key = input()
    if key == '1':
        contador1.pause()
    elif key == '2':
        contador2.pause()
    elif key == '11':
        contador1.resume()
    elif key == '22':
        contador2.resume()


