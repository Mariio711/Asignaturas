(deftemplate animal (slot nombre))
(deftemplate caracteristica (slot nombre) (slot atributo) (slot valor))
(deftemplate especie (slot animal) (slot tipo))
(deftemplate padre (slot progenitor) (slot hijo))


(deffacts hechos-iniciales
    (animal (nombre Robi))
        (caracteristica (nombre Robi) (atributo pelo) (valor si))
        (caracteristica (nombre Robi) (atributo color) (valor leonado))
        (caracteristica (nombre Robi) (atributo rayas) (valor negras))
        (caracteristica (nombre Robi) (atributo vuela) (valor no))
        (caracteristica (nombre Robi) (atributo come) (valor carne))

    (animal (nombre Susi))
        (caracteristica (nombre Susi) (atributo plumas) (valor si))
        (caracteristica (nombre Susi) (atributo color) (valor blanco))
        (caracteristica (nombre Susi) (atributo vuela-bien) (valor si))
        (caracteristica (nombre Susi) (atributo come) (valor pescado))
)

;;R1: Si un animal tiene pelo entonces es un mamífero
(defrule R1
    (caracteristica (nombre ?x) (atributo pelo) (valor si))
=>
    (assert (mamifero ?x))
)

;;R2: Si un animal da leche, entonces es mamífero
(defrule R2
    (caracteristica (nombre ?x) (atributo da-leche) (valor si))
=>
    (assert (mamifero ?x))
)

;;R3: Si un animal tiene plumas es un ave
(defrule R3
    (caracteristica (nombre ?x) (atributo plumas) (valor si))
=>
    (assert (ave ?x))
)

;;R4: Si un animal vuela y pone huevos, es ave
(defrule R4
    (caracteristica (nombre ?x) (atributo vuela-bien) (valor si))
    (caracteristica (nombre ?x) (atributo pone-huevos) (valor si))
=>
    (assert (ave ?x))
)

;;R5: Si un animal come carne, es carnívoro
(defrule R5
    (caracteristica (nombre ?x) (atributo come) (valor carne))
=>
    (assert (carnivoro ?x))
)

;;R6: Si un animal tiene dientes puntiagudos, tiene garras, tiene ojos al frente es carnívoro
(defrule R6
    (caracteristica (nombre ?x) (atributo dientes) (valor puntiagudos))
    (caracteristica (nombre ?x) (atributo garras) (valor si))
    (caracteristica (nombre ?x) (atributo ojos) (valor al-frente))
=>
    (assert (carnivoro ?x))
)

;;R7: Si un animal mamífero tiene pezuñas es una ungulado
(defrule R7
    (mamifero ?x)
    (caracteristica (nombre ?x) (atributo pezuñas) (valor si))
=>
    (assert (ungulado ?x))
)

;;R8: Si un animal mamífero rumia es un ungulado
(defrule R8
    (mamifero ?x)
    (caracteristica (nombre ?x) (atributo rumia) (valor si))
=>
    (assert (ungulado ?x))
)

;;R9: Si un animal mamífero y carnívoro tiene color leonado con manchas oscuras se trata de un leopardo
(defrule R9
    (mamifero ?x)
    (carnivoro ?x)
    (caracteristica (nombre ?x) (atributo color) (valor leonado))
    (caracteristica (nombre ?x) (atributo manchas) (valor oscuras))
=>
    (assert (leopardo ?x))
)

;;R10: Si un animal mamífero y carnívoro tiene color leonado con rayas negras es un tigre
(defrule R10
    (mamifero ?x)
    (carnivoro ?x)
    (caracteristica (nombre ?x) (atributo color) (valor leonado))
    (caracteristica (nombre ?x) (atributo rayas) (valor negras))
=>
    (assert (tigre ?x))
)

;;R11: Si un animal ungulado con cuello largo y piernas largas tienen manchas oscuras es una jirafa
(defrule R11
    (ungulado ?x)
    (caracteristica (nombre ?x) (atributo cuello) (valor largo))
    (caracteristica (nombre ?x) (atributo piernas) (valor largas))
    (caracteristica (nombre ?x) (atributo manchas) (valor oscuras))
=>
    (assert (jirafa ?x))
)

;;R12: Si un animal es un ungulado con rayas negras es una cebra
(defrule R12
    (ungulado ?x)
    (caracteristica (nombre ?x) (atributo rayas) (valor negras))
=>
    (assert (cebra ?x))
)

;;R13: Si un animal es ave y no vuela y tiene el cuello largo y piernas largas de color blanco y negro es un avestruz
(defrule R13
    (ave ?x)
    (caracteristica (nombre ?x) (atributo vuela-bien) (valor no))
    (caracteristica (nombre ?x) (atributo cuello) (valor largo))
    (caracteristica (nombre ?x) (atributo piernas) (valor largas))
    (caracteristica (nombre ?x) (atributo color) (valor blanco-negro))
=>
    (assert (avestruz ?x))
)

;;R14: Si un animal es ave, no vuela, nada, de color blanco y negro, se trata de un pingüino
(defrule R14
    (ave ?x)
    (caracteristica (nombre ?x) (atributo vuela-bien) (valor no))
    (caracteristica (nombre ?x) (atributo nada) (valor si))
    (caracteristica (nombre ?x) (atributo color) (valor blanco-negro))
=>
    (assert (pingüino ?x))
)

;;R15: Si es un ave que vuela bien y come pescado, es un albatros
(defrule R15
    (ave ?x)
    (caracteristica (nombre ?x) (atributo vuela-bien) (valor si))
    (caracteristica (nombre ?x) (atributo come) (valor pescado))
=>
    (assert (albatros ?x))
)

;;R16: Si un animal es de una especie y ese animal es padre de otro, entonces el hijo es de la misma especie.
(defrule R16
    (especie (animal ?padre) (tipo ?t))
    (padre  (progenitor ?padre) (hijo ?h))
=>
    (assert (especie (animal ?h) (tipo ?t)))
)