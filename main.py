"""
1. Que temas va a explicar tu tutor (minimo 4, de cualquier sesion 1 a 6): variable, lista, diccionario, funcion, clase, git...
Respuesta: El tutor de python deberá explicar los siguientes temas: estructura de datos con diccionarios y lista, funciones, clases e iteraciones con for sobre listas y diccionarios para captura y modificación de datos.

2. Que necesita "self" para recordar: la conversacion completa, y el resultado de cada pregunta que ya intentaron.
Respuesta: self necesitara de un historial tipo diccionario que guardara tanto la respuesta del agente como el mensaje del usuario en forma de clave-valor.

3. Si preguntan por un tema que no existe, que debe responder.
Respuesta: si se le pregunta al agente algo que no existe dentro del historial o diccionario ya pre-establecido el agente deberá responder con que no dispone de esa información y preguntar por algo mas en lo que le pueda asistir.

4. Cuando alguien responda una pregunta, como se sabe si acerto
Respuesta: las respuestas a las preguntas ya estarán almacenadas en un diccionario el cual se va a iterar y si existe dicha respuesta entonces el agente abra elegido corretamente(de manera exitosa) dicha respuesta.

"""


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
        respuesta_usuario = input(datos["pregunta"]).strip()
        if datos["tipo"] == "numero":
            try:
                acerto = int(respuesta_usuario) == int(datos["respuesta"])
            except ValueError:
                acerto = False
        else:
            acerto = respuesta_usuario.casefold() == datos["respuesta"].casefold()

        self.temas_dominados[tema_encontrado] = acerto
        if acerto:
            return f"¡Correcto! Has acertado la pregunta sobre {tema_encontrado.replace('_', ' ')}."
        return f"No es correcto. La respuesta era: {datos['respuesta']}."

    def responder(self, mensaje):
        mensaje_normalizado = str(mensaje).strip().lower()
        saludos = ("hola", "buenos dias", "buenas tardes", "buenas", "hi")
        despedidas = ("adios", "adiós", "hasta luego", "bye", "chau")

        self.historial.append({"estudiante": mensaje_normalizado})

        if any(palabra in mensaje_normalizado for palabra in saludos):
            respuesta = "¡Hola! Soy tu tutor de Python. ¿En qué tema te gustaría aprender hoy?"
        elif any(palabra in mensaje_normalizado for palabra in despedidas):
            respuesta = "¡Hasta luego! Recuerda que estoy aquí para ayudarte con Python."
        elif "pregunta" in mensaje_normalizado:
            respuesta = self.hacer_pregunta(mensaje_normalizado)
        elif "explicar" in mensaje_normalizado or "explicame"  in mensaje_normalizado or "explicas" in mensaje_normalizado:
            respuesta = self.explicar_concepto(mensaje_normalizado)
        else:
            respuesta = "No tengo información sobre ese tema. Puedes preguntarme por estructuras de datos, funciones, clases o for."

        self.historial.append({"tutor": respuesta})
        return respuesta


def main():
    tutor = TutorPython()
    print(tutor.responder("hola"))
    print(tutor.responder("¿Me explicas funciones?"))
    print(tutor.responder("hasta luego"))
    print(tutor.historial)


if __name__ == "__main__":
    main()


