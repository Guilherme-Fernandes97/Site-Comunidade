from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/contato")
def contato():
    return 'Qualquer dúvida mante um email para listavip@hashtagtreinamentos.com'

if __name__ == '__main__':
    app.run()