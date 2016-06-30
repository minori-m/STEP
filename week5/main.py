#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import webapp2
#import cgi

#class MainPage(webapp2.RequestHandler):
#    def get(self):
#        self.response.headers['Content-Type'] = 'text/plain'
#        self.response.write('こんにちは！')
#
#app = webapp2.WSGIApplication([
#    ('/', MainPage),
#], debug=True)

#
#class MainPage(webapp2.RequestHandler):
#    def get(self):
#        self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
#        self.response.write("""
#            <body>
#            <i><input type="text" name="name1"></i>
#            <i><input type="submit" name="submit"></i>
#            </body>
#            """)
#        form = cgi.FieldSorage()
#        content''
#        content+="submitted = %s<br/>"%form.getvalue('name1','')
#        print "Content-type: text/html\n"
#        print html_body %content
#
#
#app = webapp2.WSGIApplication([
#    ('/.*', MainPage),
#], debug=True)

#class Root(webapp2.RequestHandler):
#    def get(self):
#        self.response.headers['Content-Type'] = 'text/plain'
#        self.response.write('Hello,world!\n')
#
#class Test(webapp2.RequestHandler):
#    def get(self,value):
#        self.response.write('foo was set to %s' % value)
#
#app = webapp2.WSGIApplication([
#    ('/',Root),
#    ('/.*',Test)
#],debug=True)

import cgi
import webapp2
import test


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html; charset=utf-8"
        self.response.out.write("""
            <html>
            <head>
            <title>
            パタトクカシーー
            </title>
            <head>
            <body>
            <h1>２つの単語を入力してください。</h1>
            <form action="/result" method="get" accept-charset=UTF-8>
            <p><input type="text" name = "name1"></p>
            <p><input type="text" name = "name2"></p>
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
            統合結果
            </title>
            <head>
            <body>
            あわせると
            """)
        name1 = str(self.request.get("name1").encode('utf-8'))
        name2 = str(self.request.get("name2").encode('utf-8'))

#        self.response.write(name1)
        self.response.out.write(test.combine(name1,name2).encode('utf-8'))
        self.response.out.write("""です。
            </body>
            </html>
            """
                                )



app = webapp2.WSGIApplication([("/", MainPage),
                               ("/result", ResultPage)],
                              debug=True)