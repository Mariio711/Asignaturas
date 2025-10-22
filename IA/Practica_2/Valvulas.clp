(deftemplate valvula
    (slot nombre)
    (slot estado (allowed-values abierta cerrada) (default cerrada))
    (slot Te (default 0))
    (slot Ti (default 0))
    (slot presion (default 0))
)

(deffacts iniciales
    (valvula (nombre Entrada) (Te 101) (Ti 35) (presion 1))
    (valvula (nombre Salida) (Te 101) (Ti 155) (presion 5))
    (valvula (nombre Pasillo1) (Te 99) (Ti 37) (estado cerrada))
)

;;Funciones
(deffunction aumPresion (?te ?p)
    (while (> ?te 35)
        (bind ?p (+ ?p 1))
        (bind ?te (- ?te 5))
    )
    (return (create$ ?p ?te)) ;; devuelve multifield: (presion temperatura)
)

(deffunction decTemp (?te ?ti)
    (return (- ?ti ?te)) ;; devuelve multifield: (presion temperatura)
)

;;Reglas

;;Si una válvula está abierta con un valor de presión 5, entonces la válvula se cierra y se baja la presión a 0.
(defrule R1
    ?v <- (valvula (presion ?p) (estado abierta))
    (test (= 5 ?p))
=>
    (modify ?v (presion 0) (estado cerrada))
)

;;Si una v´alvula cerrada tiene un valor de presi´on menor de 10 y una temperatura T1 mayor de 35
;;grados entonces esta v´alvula deber´a abrirse y aumentar la presi´on en funci´on de la temperatura
;;T1.
(defrule R2
    ?v <- (valvula (Te ?te) (presion ?p) (estado cerrada))
    (test (> ?te 35))
    (test (< ?p 10))
=>
    (bind $?res (aumPresion ?p ?te))
    (bind ?newP (nth$ 1 $?res))
    (bind ?newTe (nth$ 2 $?res))
    (modify ?v (presion ?newP) (Te ?newTe) (estado abierta))
    (printout t "Válvula " ?newP " -> presion=" ?newP ", Te=" ?newTe crlf)
)

;;Si dos v´alvulas distintas, v1 y v2, tienen la misma temperatura T2, y la temperatura T1 de la
;;v´alvula v2, es menor que T2, entonces se decrementa la temperatura T2 de la v´alvula v2 y se
;;abren ambas v´alvulas.
(defrule R3
    ?v1 <- (valvula (Te ?te1) (Ti ?ti))
    ?v2 <- (valvula (Te ?te2) (Ti ?ti))
    (test (> ?te2 ?ti))
=>
    (bind ?newti (decTemp ?te2 ?ti))
    (modify ?v2 (Ti ?newti) (estado abierta))
    (modify ?v1 (estado abierta))
)