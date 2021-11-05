import flask 

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.Response('Bem vindo')    
    
    if __name__ == '__main__':
      app.run()