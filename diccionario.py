# Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Damaris Ulloa",       # Nombre completo de la persona
    "edad": 18,                   # Edad en años
    "ciudad": "Cuenca",           # Ciudad de residencia
    "profesion": "Ingeniera"         # Ocupación principal
}

# Actualizar la ciudad a una nueva ubicación
informacion_personal["ciudad"] = "Manta"  # Cambiamos "Cuenca" por "Manta"

# Agregar una nueva clave-valor (en este caso, actualizamos "profesion")
# NOTA: "profesion" ya existía, por lo que se actualiza su valor
informacion_personal["profesion"] = "Cirujana"  # Nueva profesión especializada

# Verificar si existe "telefono" y agregarlo si no está presente
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0968372883"  # Número ficticio de 10 dígitos

# Eliminar la clave "edad" porque no es relevante para el contexto actual
del informacion_personal["edad"]  # Removemos datos sensibles innecesarios

# Mostrar el diccionario final
print("Información personal actualizada:")
print(informacion_personal)