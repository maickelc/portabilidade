# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "maickel"
__date__ = "$09/03/2016 07:41:49$"

from flask import Flask, Response
import random


operadoras = (
    '55301',
    '55302',
    '55303',
    '55304',
    '55305',
    '55306',
    '55312',
    '55314',
    '55320',
    '55321',
    '55323',
    '55324',
    '55331',
    '55337',
    '55341',
    '55343',
    '55349',
    '55351',
    '55375',
    '55377',
    '55390',
    '55391',
    '55392',
    '55393',
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

O = Oper()

@app.route('/<int:number>')
def hello(number=None):
    operadora = O.get()
    return Response("{0}".format(operadora))

if __name__ == "__main__":
    try:
        host = '0.0.0.0'
        app.run(host=host, port=5000,debug=True)
    except KeyboardInterrupt:
        raise SystemExit
