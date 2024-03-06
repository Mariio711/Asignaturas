def imprimir_directorios_inicio():
    with open('/etc/passwd', 'r') as f:
        for linea in f:
            if not linea.startswith('#'):  # Ignorar comentarios
                partes = linea.split(':')
                print('Usuario: {}, Directorio de inicio: {}'.format(partes[0], partes[5]))

imprimir_directorios_inicio() #en mac se hace diferente