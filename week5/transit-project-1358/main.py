#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import webapp2
import network

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html; charset=utf-8"
        self.response.out.write("""
            <html>
            <head>
            <title>
            transit in Wonderland
            </title>
            <head>
            <body>
            <h1>Input the departure station and the arrival station.</h1>
            <form action="/result" method="get" accept-charset=UTF-8>
            <p>departure<input type="text" name = "dep"></p>
            <p>arrival<input type="text" name = "arr"></p>
            <br>
            <input type="submit">
            </form>
            </body>
            </html>
            """)


class ResultPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html; charset=utf-8"
        self.response.out.write("""
            <html>
            <head>
            <title>
            How to go
            </title>
            <head>
            <body>
            行き方は
            """)
        dep = str(self.request.get("dep").encode('utf-8'))
        arr = str(self.request.get("arr").encode('utf-8'))

        self.response.write(dep)
#        self.response.out.write(network.showpath(dep,arr).encode('utf-8'))
        self.response.out.write("""です。
            </body>
            </html>
            """
                                )



app = webapp2.WSGIApplication([("/", MainPage),
                               ("/result", ResultPage)],
                              debug=True)