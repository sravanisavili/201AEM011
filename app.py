from flask import Flask, request

from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate, identity
from user import UserRegister
from item import Item


app = Flask(__name__)

app.secret_key = 'Girija'

api = Api(app)

jwt = JWT(app, authenticate, identity) #JWT object is created and after that Flask_JWT registers has an endpoint

api.add_resource(Item, '/<name>')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)
    #sravani
