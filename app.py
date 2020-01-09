from flask import Flask, render_template, url_for, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class IndexView(Resource):
    def get(self, username):
        return {"username": "zxl"}


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')
# api.add_resource(HelloWorld, '/')
# api.add_resource(IndexView, '/', '/login/<username>', endpoint='index')

if __name__ == '__main__':
    app.run(debug=True)
