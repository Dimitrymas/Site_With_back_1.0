from flask import Flask
from flask import render_template, request


app = Flask(__name__)


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

    return render_template(
        'index.html',
        message=server_message, dict={'Landerix' : '1.png', 'Vasya' : 'vasya.png', 'Landerix' : '1.png', 'Vasya' : 'vasya.png'}
    )




@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/info/<nick>')
def info(nick):
    return render_template('info.html', nick=nick)



if __name__ == '__main__':
    app.run(host='localhost', port=80)