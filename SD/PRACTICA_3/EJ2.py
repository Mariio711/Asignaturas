import json

from bottle import post, run, request, response, HTTPError

#array mis_elementos
mis_elementos = []



@post ('/inserta')
def inserta():
    try:
        data = request.json
        #datos del JSON
        #comprobamos si 'elemento' esta en el JSON
        if 'elemento' in data:
            elemento = data.get('elemento')

            #comprobamos si el elemento existe en el array
            if elemento not in mis_elementos:
                mis_elementos.append(elemento)

                #enviamos respuesta con el JSON
                response.headers['Content-Type'] = 'application/json'

                response_data = {'mi lista': mis_elementos}
                return json.dumps(response_data)
        else:
            raise HTTPError(400, 'Clave "elemento" no encontrada en el JSON')
    except Exception as e:
        raise HTTPError(500, str(e))
    
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
