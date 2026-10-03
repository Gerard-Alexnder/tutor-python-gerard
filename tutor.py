class TutorPython:
    def __init__(self):
        self.historial = []
        self.temas_dominados = {}
        self.temas = {
            "estructura_de_datos": {
                "explicacion": (
                    "Las estructuras de datos en Python son formas de guardar información. "
                    "Las listas permiten ordenar elementos y los diccionarios guardan datos con clave y valor. "
                    "Ejemplo: notas = [8, 9, 10]; persona = {'nombre': 'Ana', 'edad': 20}."
                ),
                "pregunta": "¿Qué estructura guarda datos mediante pares de clave y valor? ",
                "respuesta": "diccionario",
                "tipo": "texto",
            },
            "funciones": {
                "explicacion": (
                    "Las funciones permiten reutilizar bloques de código y organizar mejor el programa. "
                    "Ejemplo: def saludar(nombre): return f'Hola, {nombre}'; saludar('Luis')."
                ),
                "pregunta": "¿Qué palabra clave se usa para definir una función en Python? ",
                "respuesta": "def",
                "tipo": "texto",
            },
            "clases": {
                "explicacion": (
                    "Las clases sirven para crear objetos con atributos y métodos. "
                    "Ejemplo: class Persona: def __init__(self, nombre): self.nombre = nombre; p = Persona('Ana')."
                ),
                "pregunta": "¿Qué palabra clave se usa para definir una clase en Python? ",
                "respuesta": "class",
                "tipo": "texto",
            },
            "for": {
                "explicacion": (
                    "El ciclo for recorre elementos de una lista o diccionario para procesarlos uno a uno. "
                    "Ejemplo: for numero in [1, 2, 3]: print(numero) y for clave, valor in {'a': 1, 'b': 2}.items(): print(clave, valor)."
                ),
                "pregunta": "¿Qué ciclo se usa para recorrer los elementos de una lista? ",
                "respuesta": "for",
                "tipo": "texto",
            },
            "lista": {
                "explicacion": "Una lista es una colección ordenada de elementos; sus posiciones empiezan en cero.",
                "pregunta": "¿En qué posición está el primer elemento de una lista? ",
                "respuesta": "0",
                "tipo": "numero",
            },
        }

    def explicar_concepto(self, mensaje_normalizado):
        for tema, datos in self.temas.items():
            palabras = tema.split("_")
            if tema.replace("_", " ") in mensaje_normalizado or all(
                palabra in mensaje_normalizado.split() for palabra in palabras
            ) or (tema == "lista" and "listas" in mensaje_normalizado.split()):
                return datos["explicacion"]
        temas_disponibles = ", ".join(tema.replace("_", " ") for tema in self.temas.keys())
        return f"No encontré ese tema. Los temas disponibles son: {temas_disponibles}."

    def hacer_pregunta(self, mensaje_normalizado):
        palabras_mensaje = mensaje_normalizado.replace("¿", " ").replace("?", " ").split()
        tema_encontrado = None
        for tema in self.temas:
            palabras_tema = tema.split("_")
            if all(palabra in palabras_mensaje for palabra in palabras_tema) or (
                tema == "lista" and "listas" in palabras_mensaje
            ):
                tema_encontrado = tema
                break

        if tema_encontrado is None:
            return "Indica el tema de la pregunta: lista, estructuras de datos, funciones, clases o for."

        datos = self.temas[tema_encontrado]
        respuesta_estudiante = input(datos["pregunta"]).strip()
        if datos["tipo"] == "numero":
            try:
                respuesta_estudiante = int(respuesta_estudiante)
            except ValueError:
                return "Por favor, responde con un número entero."
            acerto = respuesta_estudiante == int(datos["respuesta"])
        else:
            acerto = respuesta_estudiante.casefold() == datos["respuesta"].casefold()

        clave_resultado = tema_encontrado
        numero_intento = 2
        while clave_resultado in self.temas_dominados:
            clave_resultado = f"{tema_encontrado}_{numero_intento}"
            numero_intento += 1
        self.temas_dominados[clave_resultado] = acerto
        if acerto:
            return f"¡Correcto! Has acertado la pregunta sobre {tema_encontrado.replace('_', ' ')}."
        return f"No es correcto. La respuesta era: {datos['respuesta']}."

    def mostrar_progreso(self):
        if not self.temas_dominados:
            return "Todavía no has intentado ninguna pregunta."

        correctas = sum(self.temas_dominados.values())
        intentadas = len(self.temas_dominados)
        return f"Has respondido correctamente {correctas} de {intentadas} preguntas."

    def responder(self, mensaje):
        mensaje_normalizado = str(mensaje).strip().lower()
        saludos = ("hola", "buenos dias", "buenas tardes", "buenas", "hi")
        despedidas = ("adios", "adiós", "hasta luego", "bye", "chau")

        self.historial.append({"estudiante": mensaje_normalizado})

        if any(palabra in mensaje_normalizado for palabra in saludos):
            respuesta = "¡Hola! Soy tu tutor de Python. ¿En qué tema te gustaría aprender hoy?"
        elif any(palabra in mensaje_normalizado for palabra in despedidas):
            respuesta = "¡Hasta luego! Recuerda que estoy aquí para ayudarte con Python."
        elif "progreso" in mensaje_normalizado:
            respuesta = self.mostrar_progreso()
        elif "pregunta" in mensaje_normalizado:
            respuesta = self.hacer_pregunta(mensaje_normalizado)
        elif "explicar" in mensaje_normalizado or "explicame"  in mensaje_normalizado or "explicas" in mensaje_normalizado:
            respuesta = self.explicar_concepto(mensaje_normalizado)
        else:
            respuesta = "No tengo información sobre ese tema. Puedes preguntarme por estructuras de datos, funciones, clases o for."

        self.historial.append({"tutor": respuesta})
        return respuesta


    def mostrar_historial(self):
        for registro in self.historial:
            for quien, texto in registro.items():
                print(f"{quien} : {texto}")

    def iniciar_conversacion(tutor):
        print("Tutor de Python -  escribe 'salir' para terminar la conversacion\n")
        while True:
            mensaje = input("Tu: ")
            respuesta = tutor.responder(mensaje)
            print(f"Tutor: {respuesta}\n")
            if "adios" in mensaje.lower() or "salir" in mensaje.lower():
                break
            print("---Historial de la conversacion---")
            tutor.mostrar_historial()

if __name__ == "__main__":
    tutor_prueba = TutorPython()
    print("Corriendo tutor.py directamente - autoprueba:")
    print(tutor_prueba.responder("hola"))