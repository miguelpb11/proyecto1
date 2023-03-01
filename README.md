# proyecto1

utilizar modulo threading ytime para crear hilos pausarlos y reanudarlos y un tiempo definido

se crea la clase contador con:

El argumento id es un número entero que representa el numero del contador. posicion es la posición en la que se imprimirá el contador en la consola. Las variables count (el número en el contador), paused (un indicador de si el contador está pausado), pause_cond (un objeto de condición utilizado para pausar y reanudar el contador) y posicion

El método start se llama para iniciar el hilo del contador. Crea un nuevo objeto usando threading.Thread y le asigna la función run. El hilo se inicia llamando al método start del hilo.

El método run es el que se ejecuta en el hilo. Es un bucle infinito que se ejecuta hasta que se detiene el hilo. Utiliza with para adquirir el bloqueo del objeto pause_cond y pausar el hilo mientras la variable paused es True. Una vez que se reanuda el hilo, aumenta el valor del contador mas uno, lo imprime en la consola en la posición dada y espera dos segundos antes de continuar con la siguiente iteración.

Los métodos pause y resume se utilizan para pausar y reanudar el contador. El método pause establece la variable paused en True, lo que hará que el contador se detenga en la próxima repeticion del bucle. El método resume establece la variable paused en False, lo que hace que el contador continúe. Además, notifica al objeto pause_cond que se ha reanudado el hilo.

el método wait_key permite pausar y reanudar cada contador por separado. El usuario puede ingresar el número "1" para pausar contador 1 y el número "2" para pausar el contador 2.

Afuera de la clase contador,

se crean dos contadores de la clase Contador y se llama al método start en cada una de ellas. El programa esperará a que el usuario ingrese los números "1" y "2" para pausar y los numeros "11" y "22" para reanudar cada contador por separado.

Si el usuario presiona la tecla 3, se pausan ambos contadores y se espera a que los hilos terminen su ejecución llamando al método join() en ambos hilos, se muestra un mensaje de "programa finalizado" y se sale del programa con break.
