# -*- coding: utf-8 -*-
import os
import json
from flask import Flask, request, send_file
from flask import render_template

app = Flask(__name__, template_folder='templates', static_folder='static_redeploy', static_url_path='/static_redeploy')
app.jinja_env.variable_start_string = '{['
app.jinja_env.variable_end_string = ']}'

print('Waiting...')

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/redeploy/getData', methods=["GET"])
def get_data():
    with open('./data/test.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return json.dumps(data)

@app.route('/error')
def error():
    return '404 not found'


app.run(host='0.0.0.0', debug=False, port=52173)  # 52inami