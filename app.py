from flask import Flask, request #importing request library
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = [] #creating a list called items (contains a dictionary for each item)

class Item(Resource): #Let us rename our Resource as Item
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404 #setting up an error code if requested object cannot be found

    def post(self, name):
            data = request.get_json()
            item = {'name': name, 'price': data['price']} # will access the price key of a data dictionary
            items.append(item)
            return item, 201 #status code showing a successful creating of an object


class ItemList(Resource): # Our new Resource
    def get(self):
        return {'items': items} #returns a list of items (dictionary items)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items') #add a resource with a correct endpoint

app.run(port=5000, debug=True) # Makes an error (if smth goes wrong) more clear in form of html
