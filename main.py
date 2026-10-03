from tutor import TutorPython
from conversacion import iniciar_conversacion

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




def main():
    tutor = TutorPython()
    tutor.iniciar_conversacion()


if __name__ == "__main__":
    main()


