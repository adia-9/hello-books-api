from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

#define endpoint
#with BP defining route /hello-world and it's gonna accept only GET request. ->#GET/hello-world
#Defining what http method will be used:GET
@hello_world_bp.route("/hello-world", methods=["GET"])
def get_hello_world():
    my_response = "Hello, world!"
    return my_response

@hello_world_bp.route("/hello-world/JSON", methods = ["GET"])
def hello_world_json():
    #whatever this method returns is what GET sent back as response who hit endpoint
    return { #return a dict
        "name":"Aida",
        "message":"My first message",
        "hobbies":["Coding, writing"],
    }, 201 #here goes the response code

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body