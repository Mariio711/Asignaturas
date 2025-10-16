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

;;Regla #1: Si un animal tiene pelo entonces es un mamífero
(defrule R1
    (caracteristica (nombre ?x) (atributo pelo) (valor si))
=>
    (assert (mamifero ?x)))