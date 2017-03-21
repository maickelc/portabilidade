# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "maickel"
__date__ = "$09/03/2016 07:41:49$"

from flask import Flask, Response
import random
import os
from flask_httpauth import HTTPBasicAuth

operadoras = (
#   '55301', #DATORA
#   '55302',
#   '55303',
#   '55304',
#   '55305',
#   '55306',
#   '55312',
#   '55314', #BRT
    '55320', #TIM
#   '55321',
#   '55323',
#   '55324',
#   '55331',
#   '55337',
    '55341', #VIVO
#    '55343',
#    '55349',
#    '55351', #NEXTEL
#    '55375',
#    '55377', #NEXTEL
#    '55390',
#    '55391',
#    '55392',
#    '55393',
)


lista = (
    47998760001,
    47998760002,
    47998760003,
    47998760004,
    47998760005,
    47998760006,
    47998760007,
    47998760008,
    47998760009,
    47998760010,
)


class Oper(object):
    def __init__(self):
        self.count = 0
        self.operadoras = operadoras
        self.iter = self._next()
        self.current = None

    def _next(self):
        for x in self.operadoras:
            yield x

    def get(self):
        if self.count == 0:
            try:
                self.current = next(self.iter)
            except StopIteration:
                self.iter = self._next()
                self.current = next(self.iter)
        self.count += 1
        if self.count == 10:
            self.count = 0
        return self.current

app = Flask(__name__)
auth = HTTPBasicAuth()

user = {
    "khomp": 'betinho'
}

O = Oper()

@app.route('/', methods=['POST', 'GET', 'PUT', 'DELETE'])
def index():
    global O
    O = Oper()
    return "<h2> Contadores zerados </h2>"

@auth.get_password
def get_pw(username):
    if username in user:
        return user.get(username)
    return None

@app.route('/auth/<int:number>', methods=['POST', 'GET', 'PUT', 'DELETE'])
@auth.login_required
def auth(number=None):
    global O, lista
    if number in lista:
        return Response("55301#{}".format(number))
    operadora = O.get()
    return Response("{0}".format(operadora))

@app.route('/<int:number>', methods=['POST', 'GET', 'PUT', 'DELETE'])
def hello(number=None):
    global O, lista
    if number in lista:
        return Response("55301#{}".format(number))
    operadora = O.get()
    return Response("{0}".format(operadora))

if __name__ == "__main__":
    try:
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
    except KeyboardInterrupt:
        raise SystemExit
