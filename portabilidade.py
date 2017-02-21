# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "maickel"
__date__ = "$09/03/2016 07:41:49$"

from flask import Flask, Response
import random


operadoras = (
    '55314',
    '55324',
    '55321',
    '55321',
    '55312',
    '55301',
    '55306',
    '55391',
    '55393',
    '55392',
    '55351',
    '55377',
    '55349',
    '55302',
    '55343',
    '55303',
    '55375',
    '55390',
    '55323',
    '55304',
    '55341',
    '55341',
    '55341',
    '55331',
    '55337',
    '55305',
    '55320',
)

class Oper:
    def __init__(self):
        self.count = 1
        self.oper = 1000

    def get(self):
        return random.choice(operadoras)

app = Flask(__name__)

O = Oper()

@app.route('/<int:number>')
def hello(number=None):
    operadora = O.get()
    return Response("{0}".format(operadora))

if __name__ == "__main__":
    try:
        host = '10.5.0.3'
        app.run(host=host, port=8000,debug=True)
    except KeyboardInterrupt:
        raise SystemExit
