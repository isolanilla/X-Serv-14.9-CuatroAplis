#!/usr/bin/python


operaciones = ["suma", "resta"]


class suma:

    def parse(self, peticion, rest):

        try:
            paquete = peticion.split()[1][1:]
            lista = paquete.split('/')
        except ValueError:
            return None
        if len(lista) != 3 or lista[0] not in operaciones:
            return None

        return lista

    def process(self, parsedRequest):

        if not parsedRequest:
            return ("400 Bad Request", "GO AWAY")

        (operacion, operando1, operando2) = parsedRequest

        if operacion == "suma":
            resultado = int(operando1) + int(operando2)
        elif operacion == "resta":
            resultado = int(operando1) - int(operando2)

        return ("200 OK", "<html><body><h1>" + str(resultado) + "</body></html>")
