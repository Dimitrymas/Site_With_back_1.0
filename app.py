from flask import Flask
from flask import render_template, request
import os
from os.path import dirname, join



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '.\\static\\img'
@app.route('/', methods=['get', 'post'])
def index():
    server_message = ''
    client_message = ''

    if request.method == 'POST':
        client_message = request.form.get('message')


        if client_message.lower() == 'hi':
            server_message = 'Hell1'
        elif client_message == 'mama':
            server_message = 'Privet'
        else:
            server_message = client_message
    dict = {}
    for i in os.listdir('static/img'):
        name = i.split('.')
        dict[name[0]] = name[1]
        print(name)

        name = ''

    return render_template(
        'index.html',
        message=server_message, dict=dict)






@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/info/<nick>')
def info(nick):
    return render_template('info.html', nick=nick)


@app.route('/fullimg/<img>')
def fullimg(img):
    return render_template('fullimg.html', img=img)
@app.route('/upload_img/', methods=['get', 'post'])
def add_img():
    if request.method == 'POST':
        datas = request.files['files[]']
        filename = datas.filename
        datas.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('input_file.html')



