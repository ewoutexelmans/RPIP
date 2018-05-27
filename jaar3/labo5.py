#!/usr/bin/python3
import smbus
from flask import Flask

app = Flask(__name__)

myi2c = smbus.SMBus(1)

data = myi2c.read_byte(0x14)

@app.route("/")
def show_value():
    global data
    s = "De spannig op de potentiometer is: "+ str(data)
