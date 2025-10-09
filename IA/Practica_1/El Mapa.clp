
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
;;Reglas para posicion opuestas directas
(defrule SUR
    (ubicacion ?x norte ?y)=>(assert (ubicacion ?y sur ?x))
)
(defrule ESTE
    (ubicacion ?x oeste ?y)=>(assert (ubicacion ?y este ?x))
)
;;Reglas para posicion por transitividad
(defrule NORTE_TRANSITIVO
    (ubicacion ?x norte ?y)(ubicacion ?y norte ?z)=>(assert (ubicacion ?x norte ?z))
)
(defrule OESTE_TRANSITIVO
    (ubicacion ?x oeste ?y)(ubicacion ?y oeste ?z)=>(assert (ubicacion ?x oeste ?z))
)
(defrule SUR_TRANSITIVO
    (ubicacion ?x sur ?y)(ubicacion ?y sur ?z)=>(assert (ubicacion ?x sur ?z))
)
(defrule ESTE_TRANSITIVO
    (ubicacion ?x este ?y)(ubicacion ?y este ?z)=>(assert (ubicacion ?x este ?z))
)
;;Relaciones derivadas
(defrule NOROESTE
    (ubicacion ?x norte ?y)(ubicacion ?x oeste ?z)=>(assert (ubicacion ?x noroeste ?z))
)
(defrule NORESTE
    (ubicacion ?x norte ?y)(ubicacion ?x este ?z)=>(assert (ubicacion ?x noreste ?z))
)
(defrule SUROESTE
    (ubicacion ?x sur ?y)(ubicacion ?x oeste ?z)=>(assert (ubicacion ?x suroeste ?z))
)
(defrule SURESTE
    (ubicacion ?x sur ?y)(ubicacion ?x este ?z)=>(assert (ubicacion ?x sureste ?z))
)
;;Transitividad de las relaciones derivadas
(defrule NOROESTE_TRANSITIVO
    (ubicacion ?x noroeste ?y)(ubicacion ?x noroeste ?z)=>(assert (ubicacion ?x noroeste ?z))
)
(defrule NORESTE_TRANSITIVO
    (ubicacion ?x noreste ?y)(ubicacion ?x noreste ?z)=>(assert (ubicacion ?x noreste ?z))
)
(defrule SUROESTE_TRANSITIVO
    (ubicacion ?x suroeste ?y)(ubicacion ?x suroeste ?z)=>(assert (ubicacion ?x suroeste ?z))
)
(defrule SURESTE_TRANSITIVO
    (ubicacion ?x sureste ?y)(ubicacion ?x sureste ?z)=>(assert (ubicacion ?x sureste ?z))
)
;;fonmateo de la entrada
(defrule inicio
    ?f1 <-(situacion ?x ?y)
    (ubicacion ?x ?u ?y)
=>
    (printout t ?x" esta al "?u" de " ?y crlf)
    (retract ?f1)
)