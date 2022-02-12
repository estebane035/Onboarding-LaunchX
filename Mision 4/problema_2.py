# Datos con los que vas a trabajar
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

titulo = f'Datos de gravedad sobre {name}'
hechos = f""" {'-'*80} 
Nombre del planeta: {planet}
Gravedad en {name}: {gravity * 1000} m/s2
"""

template = f"""{titulo.title()} 
{hechos} 
""" 

print(template)

new_template = f"""
Datos de Gravedad sobre: {name}
-------------------------------------------------------------------------------
Nombre del planeta: {planet}
Gravedad en {name}: {gravity} m/s2
"""

# Nuevos datos muestra
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'
print(new_template.format(name=nombre, planet=planeta, gravity=gravedad))

