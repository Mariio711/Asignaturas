from dataclasses import dataclass
from dbm import _Database
import json
from bottle import get, put, post, run, request, response, HTTPError

database = dict() #simulamos base de datos

#creamos la clase
class Habitacion:
    def __init__(self, id, plazas, equip = None, ocupada = False) -> None:
        self.id = id
        self.plazas = plazas
        self.equip = equip if equip is not None else []
        self.ocupada = ocupada

#dar de alta nueva habitacion
@post ('/AddRoom')
def addroom():
    try: 
        data = request.json

        #datos del json
        id = data.get('id')

        #comprueba si el id ya existe en la base de datos
        if id in database:
            raise HTTPError(400, 'Ya hay una habitacion con ese "ID"')

        if id in data:
            plazas = data.get('plazas')
            equip = data.get('equipamiento')
            equip = equip.split(',') if equip else [] #convertimos la cadena en una lista

            #crea una nueva instancia de habitacion
            habitacion = Habitacion(id, plazas, equip)

            #añadimos la habitacion a la base de datos simulada
            database[id] = habitacion

            # envía una respuesta al cliente
            response.headers['Content-Type'] = 'application/json'
            return json.dumps({'message': 'Habitacion agregada correctamente'})
        else:
            raise HTTPError(400, 'Ya hay una habitacion con ese "ID"')
    except Exception as e:
        raise HTTPError(500, str(e))

#modificar los datos de una habitacion
@put ('/UpdateRoom/<RoomId>')
def modif(RoomId):
    try:
        # verifica si la habitacion existe
        if RoomId not in database:
            raise HTTPError(404, 'Habitacion no encontrada')

        habitacion = database[RoomId]
        new = request.json

        # actualiza los valores si estan presentes en el JSON
        if 'plazas' in new:
            habitacion.plazas = new.get('plazas')
        if 'equipamiento' in new:
            habitacion.equip = new.get('equipamiento')
        if 'ocupada' in new:
            habitacion.ocupada = True if new.get('ocupada') == 'si' else False

        # formatea la salida y devuelve el json
        dict_to_parse = {'ID': RoomId, 'Plazas': habitacion.plazas, "Equipamiento": habitacion.equip, "Ocupada": 'si' if habitacion.ocupada else 'no'}
        return json.dumps(dict_to_parse)

    except Exception as e:
        raise HTTPError(500, str(e))

#consultar lista completa de habitaciones
@get ('/Rooms')
def mostrar_habitaciones():
    habitaciones = []

    for id, habitacion in database.items():
        habitaciones.append({
            'ID': id,
            'Plazas': habitacion.plazas,
            'Equipamiento': habitacion.equip,
            'Ocupada': 'si' if habitacion.ocupada else 'no'
        })

    return json.dumps(habitaciones)

#consultar habitacion mediante identificador
@get ('/Rooms/<RoomId>')
def mostrar_habitacion(RoomId):
    if RoomId not in database:
        raise HTTPError(404, 'Habitacion no encontrada')

    habitacion = database[RoomId]

    return json.dumps({
        'ID': RoomId,
        'Plazas': habitacion.plazas,
        'Equipamiento': habitacion.equip,
        'Ocupada': 'si' if habitacion.ocupada else 'no'
    })

#consultar habitaciones ocupadas o desocupadas
@get ('/Rooms/<status>')
def mostrar_habitaciones_por_estado(status):
    habitaciones = []

    for id, habitacion in database.items():
        if status == 'occupied' and habitacion.ocupada:
            habitaciones.append({
                'ID': id,
                'Plazas': habitacion.plazas,
                'Equipamiento': habitacion.equip,
                'Ocupada': 'si'
            })
        elif status == 'unoccupied' and not habitacion.ocupada:
            habitaciones.append({
                'ID': id,
                'Plazas': habitacion.plazas,
                'Equipamiento': habitacion.equip,
                'Ocupada': 'no'
            })

    return json.dumps(habitaciones)