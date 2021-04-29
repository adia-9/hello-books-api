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
    return {
        "name":"Aida",
        "message":"My first message",
        "hobbies":["Coding, writing"],
    }, 201