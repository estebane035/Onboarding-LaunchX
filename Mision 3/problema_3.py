# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.

asteroid_velocity = 25
asteroid_size = 40

if asteroid_size > 25 and asteroid_size < 1000:
    print("Cuidado un asteroide grande se acerca a la tierra!")

if asteroid_velocity > 25:
    print("El asteroide se acerca muy rapido!")
elif asteroid_velocity >= 20:
    print("Se ve la luz del asteroide en el cielo!")
else:
    print("No se puede ver el asteroide")