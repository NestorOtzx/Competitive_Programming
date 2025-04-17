def separar_casos_de_prueba(entrada):
    lineas = entrada.strip().split('\n')
    casos = []
    i = 0
    while i < len(lineas):
        caso = []
        caso.append(lineas[i])  # R C
        i += 1
        N = int(lineas[i])      # Número de botones
        caso.append(lineas[i])
        i += 1
        for _ in range(N):
            caso.append(lineas[i])
            i += 1
        casos.append('\n'.join(caso))
    return casos

# Leer el archivo example.in
with open('example.in', 'r') as f:
    entrada = f.read()

# Procesar casos de prueba
casos = separar_casos_de_prueba(entrada)

# Pedir número de caso al usuario
numero = int(input("Ingrese el número del caso de prueba que desea obtener: "))

# Mostrar el caso solicitado
if 1 <= numero <= len(casos):
    print(casos[numero - 1])
else:
    print("Número de caso inválido.")
