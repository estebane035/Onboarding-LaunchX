text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

# Dividimos el texto por oraciones
texto_oraciones = text.split(",")

# Define las palabras pista: average, temperature y distance suenan bien
keywords = ["average", "temperature", "distance"]

# Ciclo for para recorrer la cadena
for oracion in texto_oraciones:
    for k in keywords:
        if k in oracion:
            print("- " + oracion)

# Ciclo para cambiar C a Celsius
for oracion in texto_oraciones:
    for k in keywords:
        if k in oracion:
            print(oracion.replace(' C', ' Celcius'))