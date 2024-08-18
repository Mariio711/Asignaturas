# -*- coding: utf-8 -*-
import requests
import json

def mostrar_habitaciones(habitaciones):
    for habitacion in habitaciones:
        print(f"Habitacion ID: {habitacion['ID']}")
        print(f"Plazas: {habitacion['Plazas']}")
        print(f"Equipamiento: {habitacion['Equipamiento']}")
        print(f"Ocupada: {'Si' if habitacion['Ocupada'] else 'No'}")
        print("-------------------------")

def alta():
    print('Introduce los datos de la habitacion:\n')
    id = str(input('¿Que ID o numero de habitacion quieres anhadir?\n'))
    plazas = str(input('¿Cuantas plazas tiene la habitacion?\n'))
    equipamiento = str(input('¿De que equipamiento dispone? (Introduzca los campos separados por una coma (","))\n'))

    data = {
        "id": id,
        "plazas": plazas,
        "equipamiento": equipamiento
    }

    response = requests.post('http://localhost:8080/AddRoom', headers={"Content-Type": "application/json"}, data=json.dumps(data))

    # Imprime la respuesta
    print(response.json())

def modif():
    id = str(input('Introduce el ID de la habitacion que quieres modificar\n'))
    print('Introduce los nuevos datos de la habitacion:\n')
    plazas = str(input('¿Cuantas plazas tiene la habitacion?\n'))
    equipamiento = str(input('¿De que equipamiento dispone? (Introduzca los campos separados por una coma (","))\n'))
    ocupada = str(input('¿Esta ocupada?(si o no)\n'))
    ocupada = True if ocupada == 'si' else False

    data = {
        "plazas": plazas,
        "equipamiento": equipamiento,
        "ocupada": ocupada
    }

    response = requests.put(f'http://localhost:8080/UpdateRoom/{id}', headers={"Content-Type": "application/json"}, data=json.dumps(data))

    # Imprime la respuesta
    mostrar_habitaciones(response.json())


def habitaciones():
    response = requests.get('http://localhost:8080/Rooms')

    try:
        data = response.json()
    except json.JSONDecodeError:
        print("La respuesta no es un JSON válido:", response.text)
    
    # Imprime la respuesta
    mostrar_habitaciones(data)

def habitacion_id():
    id = str(input('Introduce el ID de la habitacion que quieres ver\n'))
    response = requests.get(f'http://localhost:8080/Room/{id}')

    try:
        data = response.json()
    except json.JSONDecodeError:
       print("La respuesta no es un JSON válido:", response.text)
    
    # Imprime la respuesta
    mostrar_habitaciones(data)

def habitacion_ocupada():
    resp = str(input('\t1. Habitaciones ocupadas\n\t2. Habitaciones desocupadas\n\t3. Volver'))

    if resp == 1:
        response = requests.get('http://localhost:8080/Rooms/occupied')
    elif resp == 2:
        response = requests.get('http://localhost:8080/Rooms/unoccupied')
    else:
        return
    
    try:
        data = response.json()
    except json.JSONDecodeError:
        print("La respuesta no es un JSON válido:", response.text)
    
    # Imprime la respuesta
    mostrar_habitaciones(data)

def menu_inicio():
    while True:
        print('\n\tElige una opcion:')
        print('\n\t\t1. Dar de alta una nueva habitacion')
        print('\n\t\t2. Modificar los datos de una habitacion')
        print('\n\t\t3. Consultar lista completa de habitaciones')
        print('\n\t\t4. Consultar una habitacion mediante un ID')
        print('\n\t\t5. Consultar habitaciones ocupadas o desocupadas')
        print('\n\t\t6. Salir')

        opcion = str(input())

        if opcion == '1':
            alta()
        elif opcion == '2':
            modif()
        elif opcion == '3':
            habitaciones()
        elif opcion == '4':
            habitacion_id()
        elif opcion == '5':
            habitacion_ocupada()
        elif opcion == '6':
            print('\nSaliendo del programa...')
            break
        else:
            print('\nOpcion no reconocida. Intentelo de nuevo...')


if __name__ == '__main__':
    menu_inicio()
    
