import os
import json
import random
import string
import requests
import time
from datetime import datetime

import traceback
from flask import Flask, session, request, make_response, jsonify, render_template, Response, redirect, url_for

# Crear el server Flask
app = Flask(__name__)

# Clave que utilizaremos para encriptar los datos
app.secret_key = "flask_session_key_inventada"


LOGIN_PASSWORD = "entropia"

# ------------ Views ----------------- #

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Deslogarse
    if 'user' in session:
        session.pop('user', None)
    return redirect(url_for('login'))

@app.route("/")
def index():
    try:
        if 'user' not in session:
            return redirect(url_for('login'))
        usuario = session["user"]
        return render_template('index.html', usuario=usuario)
    except Exception as e:
        print(e)
        print(jsonify({'trace': traceback.format_exc()}))
        return Response(status=400)

# ---------------- API ------------------------
@app.route('/api/v1.0/login', methods=['POST'])
def api_login():
    try:
        # Validate request data format
        content_type = request.headers.get('Content-Type')
        if ('application/x-www-form-urlencoded' not in content_type and
            'multipart/form-data' not in content_type ):
            return Response(status=415)

        # Read data
        usuario = request.form['usuario']
        password = request.form['password']

        # Process request
        if password != LOGIN_PASSWORD:
            print("LOGIN_PASSWORD incorrect")
            return Response(status=401)

        url = "http://23.92.69.190/administracion/usuarios/exists/"
        payload = {"username": usuario}
        res = requests.post(url, data=json.dumps(payload), headers={"Content-Type":"application/json"})
        if res.status_code != 200:
            print("USER incorrect")
            return Response(status=401)

        session['user'] = usuario
        return Response(status=200)

    except Exception as e:
        print(e)
        print(jsonify({'trace': traceback.format_exc()}))
        return Response(status=401)


if __name__ == '__main__':
    print('Inove@Server start!')

    # Lanzar server
    app.run(host="0.0.0.0", port=5015)
