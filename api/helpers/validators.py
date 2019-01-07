from functools import wraps
import string
import re
from flask import request,jsonify
import datetime


example_login_data = {"email":"Your email","password":"Your password"}
example_signup_data = {
    "firstName":"Your firstName", "lastName":"Your lastName", \
    "otherName":"Your otherName", "email":"Your email", \
    "phoneNumber":"Your phoneNumber", "password":"Your password", \
    "userName":"Your userName"
    }
example_create_data = {"comment": "comment","images": "image name",
        "latitude": 0.111111,"longititude": 0.1111111,"videos": "video name"}
invalid_key_msg = "Invalid Key in data,please provide valid input data"
required_feild = "field is Required"
Invalid_value_msg = "Invalid value in data,please provide valid input data"




def get_firstName(firstName):
    data = request.get_json()
    if not data["firstName"]:
        return jsonify({"message":"firstName feild is required"}), 406
    if not data["firstName"].isalpha():
        return jsonify({"message":"{} string at firstName".format(Invalid_value_msg)}), 406

def get_lastName(lastName):
    data = request.get_json()
    if not data["lastName"]:
        return jsonify({"message":"lastName feild is required"}), 406
    if not data["lastName"].isalpha():
        return jsonify({"message":"{} string at lastName".format(Invalid_value_msg)}), 406

def get_otherName(otherName):
    data = request.get_json()
    if not isinstance(data["otherName"],str):
        return jsonify({"message":"Invalid, otherName must be a string"}),406


def get_password(password):
    data = request.get_json()
    if len(data["password"]) < 6:
        return jsonify({"message":"Password must be atleast six characters or more"}), 406
    if not data["password"]:
        return jsonify({"message":"password {}".format(required_feild)}), 406

def get_email(email):
    data = request.get_json()
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", data["email"]):
        return jsonify({"message":"Your email address is not valid."}), 406

def get_userName(userName):
    data = request.get_json()
    if not data["userName"]:
        return jsonify({"message":"userName {}".format(required_feild)}), 406
    if not data["userName"].isalpha():
        return jsonify({"message":"{} at userName".format(Invalid_value_msg)}), 406

def get_phoneNumber(phoneNumber):
    data = request.get_json()
    if not data["phoneNumber"]:
        return jsonify({"message":"phoneNumber feild is required"}), 406
    if not isinstance(data["phoneNumber"],int):
        return jsonify({"error":"Invalid, must be a phone number"}), 406



def verify_login_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.data:
            return jsonify({"message": "Please provide data",
                "example":example_login_data}),400
        # if data is not of type application/json
        try:
            data = request.get_json()
            get_password(data["password"])
            get_email(data["email"])
        # if does not contain valid keys
        except KeyError:
            return jsonify({"message":invalid_key_msg,
                "example":example_login_data}), 400
        except AttributeError:
            return jsonify({"message":"Please provide valid field for string data",
                "example":example_login_data}),400
        except ValueError:
            return jsonify({"message":"Please provide valid data type for fields",
                "example":example_login_data}),406
        except:
            return jsonify({"message":"Please provide JSON data",
                "example":example_login_data}),400
        return func(*args , **kwargs)
    return wrapper


def verify_signup_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.data:
            return jsonify({"message": "Please provide data",
                "example":example_signup_data}),400
        # if data is not of type application/json
        try:
            data = request.get_json()
            firstName = data["firstName"]
            lastName = data["lastName"]
            otherName = data["otherName"]
            email = data["email"]
            password = data["password"]
            phoneNumber = data["phoneNumber"]
            userName = data["userName"]
            get_firstName(firstName)
            get_lastName(lastName)
            get_otherName(otherName)
            get_password(password)
            get_email(email)
            get_userName(userName)
            get_phoneNumber(phoneNumber)
        # if does not contain valid keys
        except KeyError:
            return jsonify({"message":invalid_key_msg,
                "example":example_signup_data}), 400
        except AttributeError:
            return jsonify({"message":"Please provide valid field for string data",
                "example":example_signup_data}),400
        except ValueError:
            return jsonify({"message":"Please provide valid data type for fields",
                "example":example_signup_data}),400
        except:
            return jsonify({"message":"Please provide JSON data",
                "example":example_signup_data}),400
        return func(*args , **kwargs)
    return wrapper



def get_longititude(longititude):
    data = request.get_json()
    if not data["longititude"]:
        return jsonify({"message":"longititude feild is required"}), 406
    if isinstance(data["longititude"],float):
        return jsonify({"message":"Invalid, longititude must be a float"}),406

def get_latitude(latitude):
    data = request.get_json()
    if not data["latitude"]:
        return jsonify({"message":"latitude feild is required"}), 406
    if isinstance(data["latitude"],float):
            return jsonify({"message":"Invalid, latitude must be a float"}),406

def get_comment(comment):
    data = request.get_json()
    if not data["comment"]:
        return jsonify({"message":"comment feild is required"}), 406
    if not isinstance(data["comment"],str):
        return jsonify({"message":"Invalid, comment must be a string"}),406

def get_status_View(status_View):
    data = request.get_json()
    if not data["status_View"]:
        return jsonify({"message":"status_View feild is required"}), 406
    if not data["status_View"].isalpha():
        return jsonify({"message":"{} string at status_View".format(Invalid_value_msg)}), 406

def get_comment(comment):
    data = request.get_json()
    if not data["comment"]:
        return jsonify({"message":"comment feild is required"}), 406
    if not isinstance(data["comment"],str):
        return jsonify({"message":"Invalid, comment must be a string"}),406

def verify_create_incident_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.data:
            return jsonify({"message": "Please provide data",
                "example":example_create_data}),400
        # if data is not of type application/json
        try:
            data = request.get_json()
            longititude=data["longititude"]
            latitude=data["latitude"]
            images=data['images']
            videos=data['videos']
            comment=data['comment']
            get_longititude(longititude)
            get_latitude(latitude)
            # get_images(images)
            # get_videos(videos)
            get_comment(comment)
        # if does not contain valid keys
        except KeyError:
            return jsonify({"message":invalid_key_msg,
                "example":example_create_data}), 400
        except AttributeError:
            return jsonify({"message":"Please provide valid field for string data",
                "example":example_create_data}),400
        except ValueError:
            return jsonify({"message":"Please provide valid data type for fields",
                "example":example_create_data}),400
        # except:
        #     return jsonify({"message":"Please provide JSON data",
        #         "example":example_create_data}),400            
        return func(*args, **kwargs)
    return wrapper
