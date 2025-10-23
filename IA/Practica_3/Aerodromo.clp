(deftemplate aeronaves
    (slot Id)
    (slot Compania)
    (slot Origen)
    (slot Destino)
    (slot VelActual)
    (slot Peticion (allowed-values Ninguna Despegue Aterrizaje Emergencia Rumbo))
    (slot Estado (allowed-values EnTierra Ascenso Crucero Descenso)(default EnTierra))
)

(deftemplate Peticion_Autorizada
    (slot IdAeronave)
)

(deftemplate aerodromo
    (slot Id)
    (slot Ciudad)
    (slot Radar (allowed-values ON OFF)) 
    (slot Visibilidad)
    (slot Viento)
)

(deftemplate piloto
    (slot IdAeronave)
    (slot Estado (allowed-values OK SOS Ejecutando Stand-by) (default Stand-by))
)

(deftemplate vuelos
    (slot IdOrigen)
    (slot IdDestino)
    (slot Distancia)
    (slot VelDespegue (default 240))
    (slot VelCrucero (default 700))
)

(deftemplate meteorologia
    (slot IdAerodromo)
    (slot Tiempo (allowed-values Lluvia Niebla Nieve VientoHuracanado Despejado))
    (slot Restringir (allowed-values Si No))
)


; Hechos iniciales para aeronaves
(deffacts iniciales
    (aeronaves (Id FX220) (Compania IB) (Origen MAD) (Destino BCN) (VelActual 0) (Peticion Despegue) (Estado EnTierra))
    (aeronaves (Id FX221) (Compania IB) (Origen BCN) (Destino VLC) (VelActual 0) (Peticion Despegue) (Estado EnTierra))
    (aeronaves (Id FX222) (Compania IB) (Origen AGP) (Destino AGP) (VelActual 0) (Peticion Despegue) (Estado EnTierra))
    (aeronaves (Id FX223) (Compania IB) (Origen BIO) (Destino BIO) (VelActual 0) (Peticion Despegue) (Estado EnTierra))
    (aeronaves (Id FX224) (Compania IB) (Origen MAD) (Destino PMI) (VelActual 0) (Peticion Despegue) (Estado EnTierra))


    ; Hechos iniciales para pilotos

    (piloto (IdAeronave FX220) (Estado Stand-by))
    (piloto (IdAeronave FX221) (Estado OK))
    (piloto (IdAeronave FX222) (Estado OK))
    (piloto (IdAeronave FX223) (Estado Stand-by))
    (piloto (IdAeronave FX224) (Estado OK))


    ; Hechos iniciales para vuelos

    (vuelos (IdOrigen MAD) (IdDestino BCN) (Distancia 880) (VelDespegue 240) (VelCrucero 800))
    (vuelos (IdOrigen BCN) (IdDestino VLC) (Distancia 300) (VelDespegue 240) (VelCrucero 700))
    (vuelos (IdOrigen AGP) (IdDestino AGP) (Distancia 500) (VelDespegue 240) (VelCrucero 750))
    (vuelos (IdOrigen BIO) (IdDestino BIO) (Distancia 400) (VelDespegue 240) (VelCrucero 720))
    (vuelos (IdOrigen MAD) (IdDestino PMI) (Distancia 600) (VelDespegue 240) (VelCrucero 780))


    ; Hechos iniciales para aeródromos

    (aerodromo (Id MAD) (Ciudad Madrid) (Radar ON) (Visibilidad 10) (Viento 60))
    (aerodromo (Id BCN) (Ciudad Barcelona) (Radar ON) (Visibilidad 80) (Viento 40))
    (aerodromo (Id VLC) (Ciudad Valencia) (Radar ON) (Visibilidad 6) (Viento 30))
    (aerodromo (Id AGP) (Ciudad Malaga) (Radar ON) (Visibilidad 6) (Viento 220))
    (aerodromo (Id BIO) (Ciudad Bilbao) (Radar OFF) (Visibilidad 6) (Viento 60))

    ; HEchos iniciales de meteorologia

    (meteorologia (IdAerodromo MAD) (Tiempo Despejado) (Restringir Si))
    (meteorologia (IdAerodromo BCN) (Tiempo Niebla) (Restringir No))
    (meteorologia (IdAerodromo VLC) (Tiempo Lluvia) (Restringir No))
    (meteorologia (IdAerodromo AGP) (Tiempo VientoHuracanado) (Restringir No))
    (meteorologia (IdAerodromo BIO) (Tiempo Niebla) (Restringir No))
)

;; Funciones auxiliares
(deffunction calcular-tiempo-horas (?distancia ?velCrucero)
    (div ?distancia ?velCrucero)
)

(deffunction calcular-tiempo-minutos (?distancia ?velCrucero)
    (mod (round (* (/ ?distancia ?velCrucero) 60)) 60)
)

;;Reglas
(defrule Alerta_Meteorologica
    (declare (salience 20))
    ?aeronave <- (aeronaves (Id ?idAeronave) (Peticion Despegue) (Origen ?origen))
    (meteorologia (IdAerodromo ?origen) (Restringir Si))
    ?piloto <- (piloto (IdAeronave ?idAeronave) (Estado ?e))
=>
    (modify ?aeronave (Peticion Ninguna))
    (modify ?piloto (Estado Stand-by))
    (println "Alerta: Despegue CANCELADO por condiciones climaticas adversas")
)

(defrule PeticionDespegue
    (declare (salience 5))
    ?aeronave <- (aeronaves (Id ?idAeronave) (Estado EnTierra) (Peticion Despegue) (Origen ?origen) (Destino ?destino))
    ?piloto <- (piloto (IdAeronave ?idAeronave) (Estado OK))
    ?aerodromo <- (aerodromo (Id ?origen) (Radar ON) (Visibilidad ?vis) (Viento ?viento))
    (test (> ?vis 5))
    (test (< ?viento 75))
    ?vuelo <- (vuelos (IdOrigen ?origen) (IdDestino ?destino) (VelDespegue ?velDespegue))
    (meteorologia (IdAerodromo ?origen) (Restringir No))
    (not (Peticion_Autorizada (IdAeronave ?idAeronave)))
=>
    (assert (Peticion_Autorizada (IdAeronave ?idAeronave)))
    (printout t "Autorización de despegue concedida para la aeronave " ?idAeronave crlf)
)

(defrule PilotoAsociado
    (declare (salience 10))
    ?aeronave <- (aeronaves (Id ?idAeronave) (Estado EnTierra) (Peticion Despegue) (Origen ?origen) (Destino ?destino) (Compania ?compania))
    ?piloto <- (piloto (IdAeronave ?idAeronave) (Estado OK))
    ?aerodromo <- (aerodromo (Id ?origen))
=>
    (printout t "COMPROBACION CORRECTA: El piloto de la aeronave " ?idAeronave " de la compañía " ?compania " se encuentra disponible para iniciar el despegue desde el aeródromo " ?origen " con destino " ?destino crlf)
)

(defrule Despegue
    (declare (salience 5))
    ?aeronave <- (aeronaves (Id ?idAeronave) (Estado EnTierra) (Peticion Despegue) (Origen ?origen) (Destino ?destino))
    ?piloto <- (piloto (IdAeronave ?idAeronave) (Estado OK))
    ?aerodromo <- (aerodromo (Id ?origen) (Radar ON) (Visibilidad ?vis) (Viento ?viento))
    ?vuelo <- (vuelos (IdOrigen ?origen) (IdDestino ?destino) (VelDespegue ?velDespegue))
    ?peticion <- (Peticion_Autorizada (IdAeronave ?idAeronave))
    (meteorologia (IdAerodromo ?origen) (Restringir No))
    (test (> ?vis 5))
    (test (< ?viento 75))
=>
    (retract ?peticion)
    (modify ?piloto (Estado Ejecutando))
    (modify ?aeronave (Estado Ascenso) (Peticion Ninguna) (VelActual ?velDespegue))
    (printout t "Despegue ejecutado para la aeronave " ?idAeronave crlf)
)


(defrule crucero
    ?aeronave <- (aeronaves (Id ?idAeronave) (Estado Ascenso) (Destino ?destino) (VelActual ?velActual))
    ?piloto <- (piloto (IdAeronave ?idAeronave) (Estado Ejecutando))
    ?vuelo <- (vuelos (IdOrigen ?origen) (IdDestino ?destino) (VelCrucero ?velCrucero) (Distancia ?distancia))
=>
    (modify ?aeronave (Estado Crucero) (VelActual ?velCrucero))
    (modify ?piloto (Estado Stand-by))
    (bind ?tiempoVueloH (calcular-tiempo-horas ?distancia ?velCrucero))
    (bind ?tiempoVueloM (calcular-tiempo-minutos ?distancia ?velCrucero))
    (printout t "El despegue ha sido correcto. La velocidad de crucero ha sido alcanzada. El tiempo estimado de vuelo es de " ?tiempoVueloH " horas y " ?tiempoVueloM " minutos." crlf)
)