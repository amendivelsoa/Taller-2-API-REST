from flask import Flask, jsonify, render_template
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Gato(Resource):
    def get(self):
        return {'sonido': 'Miau'}

class Perro(Resource):
    def get(self):
        return {'sonido': 'Guau'}

class Huron(Resource):
    def get(self):
        return {'sonido': 'Frr'}

class BoaConstrictor(Resource):
    def get(self):
        return {'accion': 'Constricción'}

api.add_resource(Gato, '/gato')
api.add_resource(Perro, '/perro')
api.add_resource(Huron, '/huron')
api.add_resource(BoaConstrictor, '/boa')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
