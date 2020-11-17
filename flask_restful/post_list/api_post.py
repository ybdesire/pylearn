from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('task')
parser.add_argument('my_list', action='append')



# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        args = parser.parse_args()
        return {'task': args['task'], 'my_list':args['my_list'], 'http':'get'}
    def post(self):
        args = parser.parse_args()
        return {'task': args['task'], 'my_list':args['my_list'], 'http':'post'}

api.add_resource(TodoList, '/todos')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port='8002',debug=True)
