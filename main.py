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
        self.temas = {
            "estructura_de_datos": (
                "Las estructuras de datos en Python son formas de guardar información. "
                "Las listas permiten ordenar elementos y los diccionarios guardan datos con clave y valor. "
                "Ejemplo: notas = [8, 9, 10]; persona = {'nombre': 'Ana', 'edad': 20}."
            ),
            "funciones": (
                "Las funciones permiten reutilizar bloques de código y organizar mejor el programa. "
                "Ejemplo: def saludar(nombre): return f'Hola, {nombre}'; saludar('Luis')."
            ),
            "clases": (
                "Las clases sirven para crear objetos con atributos y métodos. "
                "Ejemplo: class Persona: def __init__(self, nombre): self.nombre = nombre; p = Persona('Ana')."
            ),
            "for": (
                "El ciclo for recorre elementos de una lista o diccionario para procesarlos uno a uno. "
                "Ejemplo: for numero in [1, 2, 3]: print(numero) y for clave, valor in {'a': 1, 'b': 2}.items(): print(clave, valor)."
            ),
        }

    def responder(self, mensaje):
        mensaje_normalizado = str(mensaje).strip().lower()
        saludos = ("hola", "buenos dias", "buenas tardes", "buenas", "hi")
        despedidas = ("adios", "adiós", "hasta luego", "bye", "chau")

        self.historial.append({"estudiante": mensaje_normalizado})

        if any(palabra in mensaje_normalizado for palabra in saludos):
            respuesta = "¡Hola! Soy tu tutor de Python. ¿En qué tema te gustaría aprender hoy?"
        elif any(palabra in mensaje_normalizado for palabra in despedidas):
            respuesta = "¡Hasta luego! Recuerda que estoy aquí para ayudarte con Python."
        elif "lista" in mensaje_normalizado or "diccionario" in mensaje_normalizado or "estructura" in mensaje_normalizado:
            respuesta = self.temas["estructura_de_datos"]
        elif "funcion" in mensaje_normalizado:
            respuesta = self.temas["funciones"]
        elif "clase" in mensaje_normalizado:
            respuesta = self.temas["clases"]
        elif "for" in mensaje_normalizado or "iteracion" in mensaje_normalizado or "iteraciones" in mensaje_normalizado:
            respuesta = self.temas["for"]
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
