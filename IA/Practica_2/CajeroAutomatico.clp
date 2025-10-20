(defglobal  ?*ANNO* = 2024
            ?*LIMITE1* = 5000)

(deftemplate usuario
    (slot dni)
    (slot pin)
    (slot cashout(default 0))    
)

(deftemplate tarjeta
    (slot dni)
    (slot pin)
    (slot intentos (default 3))
    (slot limite (default 3000))
    (slot validada (default SI)(allowed-values SI NO))
    (slot anno (default 2030))
)

(deftemplate cuenta
    (slot dni)
    (slot saldo)
    (slot estado(allowed-values enPantalla dineroEntregado Inicial SuperaLimite SinSaldo)(default Inicial))
)


;;Datos iniciales
(deffacts iniciales
    (tarjeta (dni 123456) (pin 1212) (intentos 3) (limite 500) (anno 2026))
    (tarjeta (dni 456456) (pin 4545) (intentos 3) (limite 500) (anno 2026))
    (tarjeta (dni 000111) (pin 0011) (intentos 0) (limite 500) (anno 2026))

    (cuenta (dni 123456) (saldo 5000))
    (cuenta (dni 456456) (saldo 33))
    (cuenta (dni 000111) (saldo 30000))
)


;;Funciones auxiliares
(deffunction decrementar (?a)
    (if(> ?a 0)
        then (return (- ?a 1))
    else (return ?a)
    )
)

(deffunction dif (?a ?b)
    (return (- ?a ?b))
)

;;Reglas

;;Validacion de tarjeta
(defrule SuperaIntentos
    (declare (salience 100))
    (usuario (dni ?dni))
    ?f1 <- (tarjeta (dni ?dni)(intentos 0))
=>
    (printout t "Superados el numero de intentos" crlf)
    (retract ?f1)
)

(defrule PinInvalido
    (usuario (dni ?dni)(pin ?pin1))
    ?f <- (tarjeta (dni ?dni)(pin ?pin2)(intentos ?int))
    (test (not (eq ?pin1 ?pin2)))
=>
    (retract ?f)
    (assert (tarjeta (dni ?dni)(pin ?pin2) (intentos (decrementar ?int))(validada NO)))
    (printout t "Pin Invalido" crlf)
)

(defrule Valida_Tarjeta
    (usuario (dni ?dni) (pin ?pin))
    (tarjeta (dni ?dni) (pin ?pin) (intentos ?int) (validada ?v) (anno ?anno))
    (test (< ?*ANNO* ?anno))
    (test (< 0 ?int))
    (test (eq ?v SI))
=>
    (printout t "Tarjeta validada" crlf)
)

;;operaciones con cuentas

