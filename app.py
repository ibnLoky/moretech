import datetime
from json import JSONEncoder
from flask import Flask
from flask import Response
import json
import db
from db import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db_parameters = db.get_db_params()
postgresDb = PostgresDB(host=db_parameters['host'],
                        port=db_parameters['port'],
                        dbname=db_parameters['dbname'],
                        user=db_parameters['user'],
                        password=db_parameters['password'])


class DateTimeEncoder(JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.__str__()

@app.route('/test_connection')
def test_connection():
    result = postgresDb.execute_querry("select 1 from videos limit 1")
    if result[0][0] == 1:
        return 'всё гуд!'
    else:
        return 'не робит'


@app.route('/')
def get_tables():
    result = postgresDb.execute_querry("select table_name from information_schema.tables where table_schema = 'public' ")
    return Response(json.dumps(result), mimetype='application/json')


@app.route('/<table>')
def get_table_columns(table):
    result = postgresDb.execute_querry(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}' ORDER BY ORDINAL_POSITION")
    return Response(json.dumps(result), mimetype='application/json')

@app.route('/<table>/<parameters>')
def get_features(table, parameters):
    parameters = (', ').join(parameters.split(','))
    result = postgresDb.execute_querry(f"SELECT {parameters} FROM {table} ")

    return Response(json.dumps(result, cls=DateTimeEncoder), mimetype='application/json')


if __name__ == '__main__':
    app.run()
