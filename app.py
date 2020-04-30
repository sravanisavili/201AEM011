from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'sravani'
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item' : None}, 404

    def post(self, name):
        data = request.get_json()
        item = {'name' : name, 'price' : data['price']}
        items.append(item)
        return item, 201
    def put(self, name):
        parser =  reqparse.RequestParser()
        parser.add_argument('price',
            type = float,
            required = True,
            help = 'This field cannot be left blank!'
        )

class Itemlist(Resource):
    def get(self):
        return {'items' : items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Itemlist, '/items')

jwt = JWT(app, authenticate, identity)

@app.route('/auth')
@jwt_required()
def auth():
    return '%s' % current_identity

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    #sravani
