from flask import Flask
from threading import Thread
from flask import jsonify
import logging

logging.basicConfig(format='[%(asctime)s] [%(threadName)s] [%(levelname)s] %(message)s', level=logging.INFO)

app = Flask('')

def fibonacci(n):              
    sequence = []              
    a, b = 0, 1              
    while len(sequence) < n:                  
        a, b = b, a + b                  
        sequence.append(a)
    return sequence

@app.route('/')
def home():
    logging.info("Root endpoint invoked")
    return  "Sample Flask REST API"

@app.route('/api/ping')
def ping():
    logging.info("Ping endpoint invoked")
    return  "Ping ok"

@app.route('/api/fibonacci/<int:num>', methods=['GET'])
def add(num):
    logging.info("Fibonacci invoked for n = %s", num)
    return jsonify({f"fibonacci({num})" : fibonacci(num)})

def run():
    app.run(host='0.0.0.0',port=8080)

t = Thread(target=run)
t.start()