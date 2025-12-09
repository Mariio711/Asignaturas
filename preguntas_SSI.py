import random
import sys

# Banco de preguntas (ampliar hasta 300)
preguntas = [
    {
        "pregunta": "¿Cuál de los siguientes tipos de hackers se caracteriza por actuar de forma legal y ética?",
        "opciones": [
            "a) White hat",
            "b) Black hat",
            "c) Grey hat",
            "d) Script kiddie"
        ],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Qué metodología de pentesting se basa en no disponer de ninguna información previa del sistema objetivo?",
        "opciones": [
            "a) Caja blanca",
            "b) Caja gris",
            "c) Caja negra",
            "d) Caja azul"
        ],
        "respuesta": "c"
    },
    {
        "pregunta": "¿Cuál de las siguientes organizaciones mantiene la base de datos CVE?",
        "opciones": [
            "a) NIST",
            "b) MITRE",
            "c) OWASP",
            "d) CERT"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Qué herramienta se utiliza para realizar ataques de fuerza bruta sobre contraseñas?",
        "opciones": [
            "a) Nessus",
            "b) John The Ripper",
            "c) Wireshark",
            "d) Nmap"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Cuál es la principal diferencia entre el cifrado simétrico y el asimétrico?",
        "opciones": [
            "a) El simétrico usa dos claves, el asimétrico una",
            "b) El simétrico usa la misma clave para cifrar y descifrar",
            "c) El asimétrico no cifra datos",
            "d) El simétrico es más lento que el asimétrico"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Qué algoritmo de cifrado utiliza LastPass para proteger sus datos?",
        "opciones": [
            "a) DES",
            "b) AES-256",
            "c) RC4",
            "d) 3DES"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Cuál es la función principal de Shodan?",
        "opciones": [
            "a) Escanear vulnerabilidades web",
            "b) Buscar dispositivos conectados a Internet",
            "c) Analizar tráfico de red",
            "d) Generar contraseñas seguras"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Qué operador de Google Dorks permite buscar archivos de un tipo específico?",
        "opciones": [
            "a) site:",
            "b) intitle:",
            "c) filetype:",
            "d) inurl:"
        ],
        "respuesta": "c"
    },
    {
        "pregunta": "¿Qué herramienta permite calcular el hash SHA-256 de un archivo desde la terminal?",
        "opciones": [
            "a) openssl",
            "b) nmap",
            "c) hydra",
            "d) metasploit"
        ],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Cuál es el propósito de la herramienta enum4linux?",
        "opciones": [
            "a) Enumerar usuarios y recursos compartidos en sistemas Windows",
            "b) Analizar tráfico de red",
            "c) Escanear puertos UDP",
            "d) Romper hashes de contraseñas"
        ],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Cuál de los siguientes protocolos se utiliza para el escaneo SYN?",
        "opciones": [
            "a) UDP",
            "b) TCP",
            "c) ICMP",
            "d) ARP"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Qué comando de Nmap realiza un escaneo tipo half-open?",
        "opciones": [
            "a) nmap -sS",
            "b) nmap -sT",
            "c) nmap -sU",
            "d) nmap -sA"
        ],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Qué tipo de ataque consiste en probar todas las combinaciones posibles de contraseñas?",
        "opciones": [
            "a) Ataque de diccionario",
            "b) Ataque por fuerza bruta",
            "c) Ataque de phishing",
            "d) Ataque de ingeniería social"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Qué es un payload en el contexto de un exploit?",
        "opciones": [
            "a) Un archivo de configuración",
            "b) El código que se ejecuta en la máquina víctima",
            "c) Una contraseña cifrada",
            "d) Un tipo de hash"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Qué operador de Google permite buscar un texto solo en el título de las páginas?",
        "opciones": [
            "a) intitle:",
            "b) inurl:",
            "c) allintext:",
            "d) filetype:"
        ],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Cuál es la principal función de la herramienta Nessus?",
        "opciones": [
            "a) Escaneo de vulnerabilidades",
            "b) Cracking de contraseñas",
            "c) Escaneo SYN",
            "d) Generación de claves RSA"
        ],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Qué comando de OpenSSL se utiliza para cifrar un archivo con AES?",
        "opciones": [
            "a) openssl enc -des",
            "b) openssl enc -aes-256-cbc",
            "c) openssl genrsa",
            "d) openssl dgst -sha256"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Qué tipo de ataque es el reverse brute force?",
        "opciones": [
            "a) Se prueban usuarios con una contraseña conocida",
            "b) Se prueban contraseñas con un usuario conocido",
            "c) Se utiliza un diccionario de palabras comunes",
            "d) Se explotan vulnerabilidades web"
        ],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Cuál es la principal diferencia entre un hash MD5 y SHA-256?",
        "opciones": [
            "a) MD5 es más seguro que SHA-256",
            "b) SHA-256 produce una salida más larga y segura",
            "c) MD5 es un algoritmo simétrico",
            "d) SHA-256 es más vulnerable a colisiones"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Qué herramienta permite realizar ataques de diccionario y fuerza bruta sobre múltiples servicios de red?",
        "opciones": [
            "a) Hydra",
            "b) Nmap",
            "c) Wireshark",
            "d) Nessus"
        ],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Qué comando de GPG se utiliza para generar un par de claves?",
        "opciones": [
            "a) gpg --gen-key",
            "b) gpg --encrypt",
            "c) gpg --decrypt",
            "d) gpg --sign"
        ],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Qué algoritmo de cifrado utiliza LastPass para proteger sus datos?",
        "opciones": ["a) DES", "b) AES-256", "c) RC4", "d) 3DES"],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Cuál es la función principal de John The Ripper?",
        "opciones": ["a) Escanear puertos", "b) Ataques de fuerza bruta a contraseñas", "c) Analizar tráfico de red", "d) Generar claves RSA"],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Qué tipo de ataque realiza John The Ripper con el archivo rockyou.txt?",
        "opciones": ["a) Ataque de diccionario", "b) Ataque de fuerza bruta", "c) Ataque de phishing", "d) Ataque de ingeniería social"],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Qué herramienta permite realizar ataques de fuerza bruta sobre múltiples servicios de red?",
        "opciones": ["a) Hydra", "b) Nmap", "c) Wireshark", "d) Nessus"],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Qué protocolo utiliza el puerto 22 para conexiones seguras?",
        "opciones": ["a) FTP", "b) Telnet", "c) SSH", "d) HTTP"],
        "respuesta": "c"
    },
    {
        "pregunta": "¿Qué herramienta se utiliza para enumerar usuarios y recursos compartidos en sistemas Windows?",
        "opciones": ["a) enum4linux", "b) Wireshark", "c) Metasploit", "d) John The Ripper"],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Qué comando de Hydra se usa para realizar un ataque de fuerza bruta con un usuario y contraseña específicos?",
        "opciones": ["a) hydra -L user.txt -P password.txt ftp://target", "b) hydra target ssh -l user -p pass -s 22 -vV", "c) hydra -h", "d) hydra --test"],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Qué herramienta permite enumerar unidades y permisos compartidos en un dominio?",
        "opciones": ["a) smbmap", "b) Nmap", "c) CrackMapExec", "d) Hydra"],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Qué tipo de ataque consiste en probar millones de nombres de usuario con una contraseña válida?",
        "opciones": ["a) Ataque de diccionario", "b) Ataque de fuerza bruta", "c) Reverse brute force", "d) Phishing"],
        "respuesta": "c"
    },
    {
        "pregunta": "¿Qué herramienta ayuda a automatizar la evaluación de seguridad en redes Active Directory?",
        "opciones": ["a) CrackMapExec", "b) enum4linux", "c) Hydra", "d) John The Ripper"],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Qué tipo de hacker es conocido por actuar a veces legalmente y a veces ilegalmente, y suele alertar a la comunidad sobre vulnerabilidades?",
        "opciones": [
            "a) White hat",
            "b) Black hat",
            "c) Grey hat",
            "d) Script kiddie"
        ],
        "respuesta": "c"
    },
    {
        "pregunta": "¿Cuál es la principal motivación de un insider para realizar ataques según la teoría?",
        "opciones": [
            "a) Reconocimiento",
            "b) Venganza o lucro",
            "c) Desafío intelectual",
            "d) Protesta social"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Qué metodología de pentesting está orientada específicamente a aplicaciones web y publica el 'Top Ten' de vulnerabilidades?",
        "opciones": [
            "a) OSSTMM",
            "b) PTES",
            "c) OWASP",
            "d) ISSAF"
        ],
        "respuesta": "c"
    },
    {
        "pregunta": "¿Cuál de las siguientes NO es una fase típica de la metodología PTES?",
        "opciones": [
            "a) Interacciones previas al compromiso",
            "b) Recopilación de inteligencia",
            "c) Explotación",
            "d) Ingeniería inversa"
        ],
        "respuesta": "d"
    },
    {
        "pregunta": "¿Qué tipo de reconocimiento implica obtener información sin interactuar directamente con el objetivo?",
        "opciones": [
            "a) Reconocimiento activo",
            "b) Reconocimiento pasivo",
            "c) Escaneo SYN",
            "d) Enumeración"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Qué herramienta permite realizar un escaneo SYN a gran velocidad y está escrita en Go?",
        "opciones": [
            "a) Nmap",
            "b) Netcat",
            "c) Furious",
            "d) Nessus"
        ],
        "respuesta": "c"
    },
    {
        "pregunta": "¿Cuál es el estado de un puerto cuando un firewall impide saber si está abierto o cerrado según Nmap?",
        "opciones": [
            "a) Abierto",
            "b) Cerrado",
            "c) Filtrado",
            "d) No-filtrado"
        ],
        "respuesta": "c"
    },
    {
        "pregunta": "¿Qué comando de Nmap realiza un escaneo tipo connect y detecta el sistema operativo?",
        "opciones": [
            "a) nmap -sS -O",
            "b) nmap -sT -O",
            "c) nmap -sU -O",
            "d) nmap -sA -O"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Qué herramienta se utiliza para descubrir dispositivos conectados a Internet y permite aplicar filtros como 'country' o 'port'?",
        "opciones": [
            "a) Shodan",
            "b) Wappalyzer",
            "c) WaybackMachine",
            "d) Phonebook.cz"
        ],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Qué operador de Google Dorks permite buscar texto concreto en el contenido de una web?",
        "opciones": [
            "a) intitle:",
            "b) inurl:",
            "c) allintext:",
            "d) filetype:"
        ],
        "respuesta": "c"
    },
    {
        "pregunta": "¿Qué tipo de ataque consiste en probar un usuario conocido con muchas contraseñas diferentes?",
        "opciones": [
            "a) Ataque de diccionario",
            "b) Reverse brute force",
            "c) Fuerza bruta simple",
            "d) Ataque de phishing"
        ],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Qué comando de John the Ripper permite usar un diccionario específico para romper contraseñas?",
        "opciones": [
            "a) john --test",
            "b) john --wordlist=diccionario.txt",
            "c) john --show",
            "d) john --format=NT"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Qué herramienta permite calcular el hash SHA-256 de un archivo en Linux?",
        "opciones": [
            "a) openssl sha1",
            "b) sha256sum",
            "c) md5sum",
            "d) hashcat"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Cuál de los siguientes algoritmos de cifrado es asimétrico?",
        "opciones": [
            "a) AES",
            "b) DES",
            "c) RSA",
            "d) Blowfish"
        ],
        "respuesta": "c"
    },
    {
        "pregunta": "¿Qué comando de GPG se utiliza para cifrar un archivo de forma simétrica?",
        "opciones": [
            "a) gpg --encrypt",
            "b) gpg -c archivo.txt",
            "c) gpg --gen-key",
            "d) gpg --sign"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Qué función tiene la firma digital en un documento?",
        "opciones": [
            "a) Garantizar la confidencialidad",
            "b) Garantizar la autenticidad e integridad",
            "c) Cifrar el contenido",
            "d) Ocultar el remitente"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Qué herramienta permite realizar ataques de fuerza bruta sobre servicios como SSH, FTP, y HTTP?",
        "opciones": [
            "a) Nessus",
            "b) Hydra",
            "c) Nmap",
            "d) Wappalyzer"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Cuál es el propósito de la herramienta enum4linux?",
        "opciones": [
            "a) Enumerar usuarios y recursos en sistemas Windows",
            "b) Escanear puertos UDP",
            "c) Romper hashes de contraseñas",
            "d) Analizar tráfico de red"
        ],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Qué base de datos contiene vulnerabilidades conocidas y es gestionada por el NIST?",
        "opciones": [
            "a) CVE",
            "b) NVD",
            "c) OWASP",
            "d) MITRE ATT&CK"
        ],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Qué herramienta se utiliza para analizar vulnerabilidades y requiere activación mediante código de licencia?",
        "opciones": [
            "a) Nessus",
            "b) Netcat",
            "c) Furious",
            "d) John the Ripper"
        ],
        "respuesta": "a"
    },
    {
        "pregunta": "¿Qué comando de OpenSSL genera un par de claves RSA?",
        "opciones": [
            "a) openssl enc -aes-256-cbc",
            "b) openssl genpkey -algorithm RSA",
            "c) openssl dgst -sha256",
            "d) openssl rsa -pubout"
        ],
        "respuesta": "b"
    },
    # ... Añade aquí hasta 300 preguntas siguiendo este formato ...
]


def realizar_test():
    random.shuffle(preguntas)
    seleccionadas = preguntas[:30]
    respuestas_usuario = []
    
    for i, pregunta in enumerate(seleccionadas, 1):
        print(f"\nPregunta {i}/30:")
        print(pregunta["pregunta"])
        for opcion in pregunta["opciones"]:
            print(opcion)
        
        while True:
            respuesta = input("\nTu respuesta (a/b/c/d): ").lower()
            if respuesta in ['a', 'b', 'c', 'd']:
                respuestas_usuario.append(respuesta)
                break
            else:
                print("Entrada inválida. Por favor, usa a/b/c/d")

    return seleccionadas, respuestas_usuario

def calcular_nota(preguntas, respuestas):
    correctas = sum(1 for p, r in zip(preguntas, respuestas) if r == p["respuesta"])
    incorrectas = len(preguntas) - correctas
    puntuacion = max(0, correctas - (incorrectas // 2))
    return (puntuacion / len(preguntas)) * 10

def mostrar_resultados(preguntas, respuestas):
    print("\n--- RESULTADOS ---")
    for i, (preg, resp) in enumerate(zip(preguntas, respuestas), 1):
        correcta = preg["respuesta"]
        estado = "✔" if resp == correcta else f"✖ (Correcta: {correcta})"
        print(f"Pregunta {i}: {estado}")
    
    nota = calcular_nota(preguntas, respuestas)
    print(f"\nNota final: {nota:.2f}/10")

def main():
    print("""
    ░██████╗░██████╗░░█████╗░██╗░░██╗███████╗
    ██╔════╝░██╔══██╗██╔══██╗██║░░██║██╔════╝
    ██║░░██╗░██████╔╝███████║███████║█████╗░░
    ██║░░╚██╗██╔══██╗██╔══██║██╔══██║██╔══╝░░
    ╚██████╔╝██║░░██║██║░░██║██║░░██║███████╗
    ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝
    """)
    
    input("Presiona Enter para comenzar el test...")
    preguntas_seleccionadas, respuestas = realizar_test()
    mostrar_resultados(preguntas_seleccionadas, respuestas)

if __name__ == "__main__":
    main()
