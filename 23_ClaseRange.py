# Clase range ------------------------------------------------------------------------------------------------

# range( stop ) con 1 argumento
# Stop: es un valor entero hasta el cual se genererá una secuencia de numeros y este numero jamas formara parte de la secuencia

# range( start, stop ) con 2 argumentos
# Start: es un valor entero que indica el numero donde se comenzara a generar la secuencia de numeros

# range( start, stop, step ) con 3 argumentos
# Step: es un valor entero que indica el incremento y decremento de la sucesion numerica entre un numero y el siguiente

# 1 argumento
range(10)          # start: 0, stop: 10, step: 0  (se genera un arngo hasta que start sea igual a stop)  -> 0 1 2 3 4 5 6 7 8 9

range(5, 11)       # start: 5, stop: 11, step: 0  -> 5 6 7 8 9 10

range( 0, 11, 2)   # start: 0, stop: 11, step: 2  -> 0 2 4 6 8 10

range( 10, 0, -1)  # start: 10, stop: 0, step: -1  -> 10 9 8 7 6 5 4 3 2 1 0
