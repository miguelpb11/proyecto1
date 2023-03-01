# proyecto1

el método wait_key permite pausar y reanudar cada contador por separado. El usuario puede ingresar el número "1" para pausar contador 1 y el número "2" para pausar el contador 2. El usuario también puede ingresar los números "11" y "22" para reanudar cada contador por separado.

El método pause simplemente establece la variable paused en True, mientras que el método resume establece la variable paused en False y notifica al hilo en espera para que reanude la ejecución.

se crean dos instancias de la clase Contador y se llama al método start en cada una de ellas. El programa esperará a que el usuario ingrese los números "1" y "2" para pausar y los numeros "11" y "22" para reanudar cada contador por separado.

La clase contador cuenta con dos argumentos id y posicion (para especificar la posicion en la pantalla donde se imprimira el contador)

El método run imprime el contador en la posición correspondiente utilizando los caracteres de control de terminal \033[{position}G que establece la posición del cursor en la columna posicion. El primer contador se muestra en la columna 1 y el segundo contador se muestra en la columna 20.

Este código es útil para aplicaciones que necesitan realizar varias tareas simultáneamente y que deben pausarse y reanudarse por separado en respuesta a eventos específicos.
