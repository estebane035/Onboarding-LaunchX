# Almacenar las entradas del usuario
factor_millas = 0.621
dis_1 = int(input("Cual es la distancia al sol del planeta 1? "))
dis_2 = int(input("Cual es la distancia al sol del planeta 2? "))

# Realizar el cálculo y determinar el valor absoluto
# Convertir de KM a Millas

dis_km = dis_2 - dis_1
print(str(dis_km) + " km")

dis_mi = dis_km * factor_millas
print(str(dis_mi) + " mi")