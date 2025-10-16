(deffacts iniciales
    (ubicacion A norte D)
    (ubicacion D norte G)
    (ubicacion B norte E)
    (ubicacion E norte H)
    (ubicacion C norte F)
    (ubicacion F norte I)
    (ubicacion A oeste B)
    (ubicacion B oeste C)
    (ubicacion D oeste E)
    (ubicacion E oeste F)
    (ubicacion G oeste H)
    (ubicacion H oeste I)
)

;; Reglas para posiciones opuestas directas (con guardas para evitar duplicados)
(defrule SUR
    (ubicacion ?x norte ?y)
=>
    (assert (ubicacion ?y sur ?x))
)

(defrule ESTE
    (ubicacion ?x oeste ?y)
=>
    (assert (ubicacion ?y este ?x))
)

;; Reglas para posicion por transitividad (con guardas)
(defrule NORTE_TRANSITIVO
    (ubicacion ?x norte ?y)
    (ubicacion ?y norte ?z)
=>
    (assert (ubicacion ?x norte ?z))
)

(defrule OESTE_TRANSITIVO
    (ubicacion ?x oeste ?y)
    (ubicacion ?y oeste ?z)
=>
    (assert (ubicacion ?x oeste ?z))
)

(defrule SUR_TRANSITIVO
    (ubicacion ?x sur ?y)
    (ubicacion ?y sur ?z)
=>
    (assert (ubicacion ?x sur ?z))
)

(defrule ESTE_TRANSITIVO
    (ubicacion ?x este ?y)
    (ubicacion ?y este ?z)
=>
    (assert (ubicacion ?x este ?z))
)

;; Relaciones derivadas (misma referencia final ?z) y sin duplicados
(defrule NOROESTE
    (ubicacion ?x este ?z)
    (ubicacion ?z norte ?y)
=>
    (assert (ubicacion ?x noroeste ?y))
)

(defrule NORESTE
    (ubicacion ?x oeste ?z)
    (ubicacion ?z norte ?y)
=>
    (assert (ubicacion ?x noreste ?y))
)

(defrule SUROESTE
    (ubicacion ?x este   ?z)
    (ubicacion ?z sur  ?y)
=>
    (assert (ubicacion ?x suroeste ?y))
)

(defrule SURESTE
    (ubicacion ?x oeste  ?z)
    (ubicacion ?z sur ?y)
=>
    (assert (ubicacion ?x sureste ?z))
)

;; Transitividad de las relaciones derivadas (encadenando por el elemento intermedio)
(defrule NOROESTE_TRANSITIVO
    (ubicacion ?x noroeste ?y)
    (ubicacion ?y noroeste ?z)
=>
    (assert (ubicacion ?x noroeste ?z))
)

(defrule NORESTE_TRANSITIVO
    (ubicacion ?x noreste ?y)
    (ubicacion ?y noreste ?z)
=>
    (assert (ubicacion ?x noreste ?z))
)

(defrule SUROESTE_TRANSITIVO
    (ubicacion ?x suroeste ?y)
    (ubicacion ?y suroeste ?z)
=>
    (assert (ubicacion ?x suroeste ?z))
)

(defrule SURESTE_TRANSITIVO
    (ubicacion ?x sureste ?y)
    (ubicacion ?y sureste ?z)
=>
    (assert (ubicacion ?x sureste ?z))
)

;; formateo de la entrada
(defrule inicio
    ?f1 <-(situacion ?x ?y)
    (ubicacion ?x ?u ?y)
=>
    (printout t ?x " esta al " ?u " de " ?y crlf)
    (retract ?f1)
)