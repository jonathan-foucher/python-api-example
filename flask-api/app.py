from flask import Flask

app = Flask(__name__)


@app.get('/my-app/hello-world-path')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
