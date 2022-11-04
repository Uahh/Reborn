# -*- coding: utf-8 -*-
import os
import json
from flask import Flask, request, send_file
from flask import render_template

app = Flask(__name__, template_folder='templates', static_folder='static_reborn', static_url_path='/static_reborn')
app.jinja_env.variable_start_string = '{['
app.jinja_env.variable_end_string = ']}'

print('Waiting...')

@app.route('/reborn', methods=["GET", "POST"])
def index():
    lang = request.args.get('lang')
    return render_template(
        'index.html',
        lang=lang
    )

@app.route('/reborn/getData', methods=["GET"])
def get_data():
    with open('./data/result.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return json.dumps(data)

@app.route('/error')
def error():
    return '404 not found'


app.run(host='0.0.0.0', debug=False, port=52173)  # 52inami
