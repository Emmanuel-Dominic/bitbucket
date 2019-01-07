import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, jsonify, request#, json, Blueprint
from api.helpers.validators import verify_create_incident_data
import datetime
# incident_bp = Blueprint('incident_bp', __name__, url_prefix='/api/v1')
app = Flask(__name__)

class DatabaseConnection:

    def __init__(self):
        """ create tables in the PostgreSQL database"""
        if os.getenv('APP_SETTINGS') == 'test_db':
            self.db = 'test_db'
            print("Hello, connected to test_db")
        else:
            self.db = 'ireporter_Database'
            print("Sorry, connected to ireporter")
            # self.db = 'dcqtq6lt2rch47'

        connection = psycopg2.connect(dbname=self.db, user='postgres', password='postgres', host='localhost', port='5432')
        # connection = psycopg2.connect(dbname=self.db, user='rzkfzvouaginmd',
                                    #   password='80d4f31f92593efe13bf6d5a51fc84b27d98e28478e877b16c5dadc637501205',
                                    #   host='ec2-54-221-207-184.compute-1.amazonaws.com', port='5432')
        connection.autocommit = True
        self.cursor = connection.cursor(cursor_factory=RealDictCursor)
        # print(self.cursor)


        # def get_incident_details(self):

db=DatabaseConnection()


def get_incidents_by_type(incident_type):
    sql_command="""SELECT incident_id,created_by,incident_Type,
            comment,status_View,images,videos,created_On,latitude,
            longititude FROM {}""".format(incident_type)
    db.cursor.execute(sql_command)
    incident=db.cursor.fetchall()
    return incident

def get_incidents_by_type_id(incident_type,incident_id):
    sql_command="""SELECT incident_id,created_by,incident_Type,
            comment,status_View,images,videos,created_On,latitude,
            longititude FROM {} WHERE incident_id='{}'""".format(incident_type,incident_id)
    db.cursor.execute(sql_command)
    incident=db.cursor.fetchone()
    return incident

def get_incidents_by_status(incident_type,incId):
    incident=get_incidents_by_type_id(incident_type,incId)
    # print(incident)
    sql_command="""SELECT incident_id,created_by,incident_Type,
            comment,status_View,images,videos,created_On,latitude,
            longititude FROM {} WHERE status_View='{}' AND incident_id={}""".format(incident_type,'draft',incId)
    db.cursor.execute(sql_command)
    incident_status=db.cursor.fetchone()
    if not incident:
    	return jsonify({"status":404, "error": "Sorry, Incident Not Found"}),404
    elif not incident_status:
   		return jsonify({"status":406, "error": "Sorry, Update not Possible"}),406

# def try_status(my_Id):
#     sql_command="""SELECT incident_id,created_by,incident_Type,
#             comment,status_View,images,videos,created_On,latitude,
#             longititude FROM {} WHERE status_View={} AND incident_id={}""".format("intervention",'draft',my_Id)
#     db.cursor.execute(sql_command)
#     incident_status=db.cursor.fetchone()
#     return incident_status

@app.route('/intervention/<int:intervention_Id>/location', methods=['PATCH'])
def update_intervention_location(intervention_Id):
    can_not_edit=get_incidents_by_status('intervention',intervention_Id)
    data = request.get_json()
    if can_not_edit:
        return can_not_edit
    elif not data:
        return "input data"
    else:
        locationLong_value = data['locationLong']
        locationLat_value = data['locationLat']
        sql_command="""UPDATE {} SET (latitude,longititude) = ({},{}) WHERE incident_id={} RETURNING incident_id""".format("intervention",locationLat_value,locationLong_value,intervention_Id)
        db.cursor.execute(sql_command)
        incident=db.cursor.fetchone()
        return  jsonify({
            "status": 200,
            "data":{"id": incident,
            "message": "Updated intervention record's location"}}), 200    

@app.route('/intervention', methods=['POST'])
@verify_create_incident_data
def Create_intervention():
    data = request.get_json()
    sql_command="""INSERT INTO intervention (incident_Id,created_By,incident_Type,comment,status_View,
        i mages,videos,created_On,latitude,longititude)
        VALUES (4,2,'interventon','{}','draft','{}','{}',now(),
        '{}','{}') RETURNING incident_id""".format(data["comment"],
        data["images"],data["videos"],data["latitude"],data["longititude"])
    db.cursor.execute(sql_command)
    incident=db.cursor.fetchone()
    return  jsonify({
        "status": 200,
        "data":{"id": incident,
        "message": "Updated intervention record's location"}}), 200    


@app.route('/<int:redflag_Id>', methods=['GET'])
# @app.route("/")
def get_specific_intervention(redflag_Id):
    intervention=get_incidents_by_type_id("intervention",int(redflag_Id))
    if intervention:
        return jsonify({
                "status": 200,
                "data": intervention
            }), 200

    return "None"

@app.route('/', methods=['GET'])
# @app.route("/")
def get_intervention():
    intervention=get_incidents_by_type("intervention")
    if intervention:
        return jsonify({
                "status": 200,
                "data": intervention
            }), 200

    return "None"



# @app.route("/")
# def index():
#     return jsonify({
#                 "IReporter": "This enables any/every citizen to bring"
#                 " any form of corruption to the notice of appropriate"
#                 " authorities and the general public."}),200



if __name__ == "__main__":
    app.run(debug=True)
    # db=DatabaseConnection()
    # db.cursor.execute("SELECT * FROM users")
    # print(db.cursor.fetchall())
    # db.cursor.execute("SELECT * FROM redflag")
    # print(db.cursor.fetchall())
    # print(try_status(1))
    