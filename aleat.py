#!/usr/bin/python


import random, webapp


class aleat(webapp.app):

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        return ("200 OK", "<html><body><h1>web generadora de URLs aleatorias !!!</h1>" +
                "<a href=http://localhost:1234/aleat/"
                + str(random.randrange(123456789)) +
                "'>dame otra</a>" +
                "</body></html>")
