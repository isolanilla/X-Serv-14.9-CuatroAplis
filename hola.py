#!/usr/bin/python


import webapp
import aleat
import suma


class hola(webapp.app):

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):

        return ("200 OK", "<html><body><h1>HOLA</body></html>")


class adios(webapp.app):

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):

        return ("200 OK", "<html><body><h1>ADIOS</body></html>")


if __name__ == "__main__":
    hola = hola()
    adios = adios()
    aleat = aleat.aleat()
    suma = suma.suma()
    classapps = {"/hola": hola, "/resta": suma, "/adios": adios, "/aleat": aleat, "/suma": suma}
    try:
        testWebApp = webapp.webApp("localhost", 1234, classapps)
    except KeyboardInterrupt:
        print "Key board interrupt"
