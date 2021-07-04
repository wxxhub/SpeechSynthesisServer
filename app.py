#coding:utf-8

from flask import (Flask, jsonify, make_response, request, send_file,
                   send_from_directory, render_template)

from src.speech_worker import SpeechWorker

import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speech_synthesis', methods=['post'])
def speech_synthesis():    
    content = request.form.get('content')
    if not content:
        return ('content is empty!')

    ok, file_name = SpeechWorker.speechSynthsis(content)

    if not ok:
        return '合成失败'
    
    path = SpeechWorker.getCachePath()
    response = make_response(send_from_directory(path,file_name.encode('utf-8').decode('utf-8'),as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(file_name.encode().decode('latin-1'))
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888')
