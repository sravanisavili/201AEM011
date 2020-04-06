from flask import Flask, jsonify,  request
from flask_restful import Resource,  Api

app = Flask(__name__)
api = Api(app)


class itemlist(Resource):
     def get(self, itemname):
          return{itemname : "Mouse, Keyboard, harddisk, RAM , Graphiccard"}

class item(Resource):
     def get(self, name):
        return{"item" : name}

     def post(self, name):
         if name == "Mouse" :
             return {"price" : "10.00"}
         elif name == "Keyboard" :
            return {"price" : "12.00"}
         elif name == "harddisk" :
            return {"price" : "14.00"}
         elif name == "RAM" :
            return {"price" : "16.00"}
         elif name == "Graphiccard" :
            return {"price" : "18.00"}


     def put(self, name):
        if name == "Mouse" :
           return {"price" : "20.00"}
        elif name == "Keyboard" :
            return {"price" : "24.00"}
        elif name == "harddisk" :
             return {"price" : "28.00"}
        elif name == "RAM" :
            return {"price" : "32.00"}
        elif name == "Graphiccard" :
           return {"price" : "36.00"}

api.add_resource(itemlist, '/<string:itemname>')
api.add_resource(item, '/item/<string:name>')


app.run(port=5000)
  #sravani
