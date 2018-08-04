from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import json

app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        return json.dumps({'employees': ['david','lili','jack']} )

class Tracks(Resource):
    def get(self):
        result = {1:'david', 2:'lili', 3:'jack'}
        return json.dumps(result)

class Employees_Name(Resource):
    def get(self, employee_id):
        employees = {1:'david', 2:'lili', 3:'jack'}
        employee_id = int(employee_id)
        if(employee_id in employees):
            return employees[employee_id]
        else:
            return 'no_employee_with_id_{0}'.format(employee_id)
        

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run(port='5002')




'''
http://127.0.0.1:5002/employees shows ids of all the employees 
http://127.0.0.1:5002/tracks shows tracks details
http://127.0.0.1:5002/employees/3 shows details of employee whose employeeid is 3
'''

