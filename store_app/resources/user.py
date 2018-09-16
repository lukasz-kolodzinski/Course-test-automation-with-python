from flask_restful import Resource, reqparse
from store_app.models.user import UserModel

class UserRegistration(Resource):
    """
        Register user bu sending a POST request with username and password
    """
    parser = reqparse.RequestParser()
    parser.add_argument("username",
                        type = str,
                        required = True,
                        help = "Type string data")
    parser.add_argument("password",
                        type = str,
                        required = True,
                        help = "This field cannot be blank")
    