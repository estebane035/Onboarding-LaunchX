# # Creamos la lista planets y la mostramos
# planets = list(["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])
# print(planets)

# # Agregamos a plutón y mostramos el último elemento
# planets.append("Pluto")
# print(planets)

# Lista de planetas
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

# Solicitamos el nombre de un planeta *Pista:  input()*
search = input("Enter the name of the planet, please use case sensitive: ")

# Busca el planeta en la lista
result_index = planets.index(search)

# Muestra los planetas más cercanos al sol
print("The planets that are closer to the sun than " + search + " are:")
print(planets[0:result_index])

# Muestra los planetas más lejanos al sol
print("The planets that are further to the sun than " + search + " are:")
print(planets[result_index+1:])