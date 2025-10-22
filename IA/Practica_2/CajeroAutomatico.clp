(defglobal  ?*ANNO* = 2025
            ?*LIMITE1* = 900)

(deftemplate usuario
    (slot dni)
    (slot pin)
    (slot cashout (default 0))    
)

(deftemplate tarjeta
    (slot dni)
    (slot pin)
    (slot intentos (default 3))
    (slot limite (default 3000))
    (slot validada (default NO)(allowed-values SI NO))
    (slot anno (default 2030))
)

(deftemplate cuenta
    (slot dni)
    (slot saldo)
    (slot estado (allowed-values enPantalla dineroEntregado Inicial SuperaLimite SinSaldo)(default Inicial))
)


;;Datos iniciales
(deffacts iniciales
    (tarjeta (dni 123456) (pin 1212) (intentos 3) (limite 500) (anno 2026))
    (tarjeta (dni 456456) (pin 4545) (intentos 3) (limite 500) (anno 2026))
    (tarjeta (dni 898111) (pin 0011) (intentos 0) (limite 500) (anno 2026))

    (cuenta (dni 123456) (saldo 5000))
    (cuenta (dni 456456) (saldo 33))
    (cuenta (dni 898111) (saldo 30000))
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
    ?u <- (usuario (dni ?dni))
    ?t <- (tarjeta (dni ?dni)(intentos 0))
=>
    (printout t "Superados el numero de intentos" crlf)
    (modify ?t (intentos 3))
    (retract ?u)

)

(defrule PinInvalido
    ?u <- (usuario (dni ?dni)(pin ?pin1))
    ?f <- (tarjeta (dni ?dni)(pin ?pin2)(intentos ?int))
    (test (not (eq ?pin1 ?pin2)))
=>
    (retract ?f)
    (assert (tarjeta (dni ?dni)(pin ?pin2) (intentos (decrementar ?int))(validada NO)))
    (printout t "Pin Invalido" crlf)
    (printout t "Introduce un pin valido :" crlf)
    (modify ?u (pin (read)))
)

(defrule Valida_Tarjeta
    (usuario (dni ?dni) (pin ?pin))
    ?t <- (tarjeta (dni ?dni) (pin ?pin) (intentos ?int) (limite ?lim) (validada NO) (anno ?anno))
    (test (< ?*ANNO* ?anno))
    (test (< 0 ?int))
=>
    (retract ?t)
    (assert (tarjeta (dni ?dni) (pin ?pin) (intentos ?int) (limite ?lim) (validada SI) (anno ?anno)))
    (printout t "Tarjeta validada" crlf)
)

;;operaciones con cuentas

;; Muesta el saldo de la cuenta asociada a la tarjeta validada
(defrule Muestra_Saldo
    (usuario (dni ?dni) (cashout ?cashout))
    (tarjeta (dni ?dni) (validada SI))
    ?f1 <- (cuenta (dni ?dni) (saldo ?saldo))
    (test (<= ?cashout ?saldo))
=>
    (printout t "Saldo de la cuenta = " ?saldo "€" crlf)
    (retract ?f1)
    (assert (cuenta (dni ?dni) (saldo ?saldo) (estado enPantalla)))
)

;;Saldo insuficiente
(defrule Saldo_NoSuficiente
    ?f1 <- (usuario (dni ?dni) (cashout ?cashout))
    (tarjeta (dni ?dni) (validada SI))
    (cuenta (dni ?dni) (saldo ?saldo))
    (test (> ?cashout ?saldo))
=>
    (printout t "Saldo de la cuenta insuficiente, no se puede realizar la operacion")
    (retract ?f1)
)


;; Comprueba limite del blanco
(defrule Comprueba_Limite1
    ?f1 <- (usuario (dni ?dni) (pin ?pin) (cashout ?cashout))
    (test (< ?*LIMITE1* ?cashout))
=>
    (retract ?f1)
    (printout t "Su peticion supera el limite establecido por el banco." crlf)
    (printout t "Introduce una cantidad inferior a " ?*LIMITE1* "€: ")
    (bind ?newcashout (read))
    (assert (usuario (dni ?dni) (pin ?pin) (cashout ?newcashout)))
)

;; Comprueba limite de la tarjeta
(defrule Comprueba_Limite2
    ?f1 <- (usuario (dni ?dni) (pin ?pin) (cashout ?cashout))
    (tarjeta (dni ?dni) (validada SI) (limite ?lim))
    (test (< ?lim ?cashout))
=>
    (retract ?f1)
    (printout t "Su peticion supera el limite establecido por la tarjeta." crlf)
    (printout t "Introduce una cantidad inferior a " ?lim "€: ")
    (bind ?newcashout (read))
    (assert (usuario (dni ?dni) (pin ?pin) (cashout ?newcashout)))
)

;; Regla de entraga del dinero 
(defrule Entrega_Dinero
    ?u <- (usuario (dni ?dni) (pin ?pin) (cashout ?cashout))
    ?t <- (tarjeta (dni ?dni) (pin ?pin) (validada SI))
    ?c <- (cuenta (dni ?dni) (saldo ?saldo))
    (test (<= ?cashout ?saldo))
=>
    (retract ?c)
    (bind ?nuevosaldo (dif ?saldo ?cashout))
    (assert (cuenta (dni ?dni) (saldo ?nuevosaldo) (estado dineroEntregado)))
    (printout t "Dinero entregado, saldo restante" ?nuevosaldo "€" crlf)
    (println "Saliendo de la cuenta..." )
    (modify ?t (validada NO))
    (retract ?u)
)

(defrule IntroducirUsuario
    (not (usuario))
=>
    (println "Introduzca el dni: ")
    (bind ?dni (read))
    (println "Introduzca el pin: ")
    (bind ?pin (read))
    (println "Introduzca la cantidad que desea extraer: ")
    (bind ?dinero (read))
    (assert (usuario (dni ?dni) (pin ?pin) (cashout ?dinero)))
)

;;Regla para si existe un usuario que no tiene cuenta ni tarjeta eliminarlo
(defrule existeUsuarioSinCuenta
    (declare (salience 10000))
    ?u <- (usuario (dni ?dni) (pin ?pin))
    (not (tarjeta (dni ?dni) (pin ?pin)))
    (not (cuenta (dni ?dni)))
=>
    (retract ?u)   
)