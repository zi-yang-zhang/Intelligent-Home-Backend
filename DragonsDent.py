from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    return app.send_static_file('view/index.html')

@app.route('/api/sendCommand')
def send():
    return

@app.route('/api/registerDevice')
def register():
    return


if __name__ == '__main__':
    app.run(debug=True)
