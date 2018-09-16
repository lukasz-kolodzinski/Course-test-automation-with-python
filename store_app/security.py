from werkzeug.security import safe_str_cmp
from store_app.models.user import UserModel

def authenticate(username, password):
    """
    Function that gets called when a users calls /auth endpoint.
    :param username: username in string format
    :param password: password (unencrypted) in string format
    :return: UserModel object onlu if authentication passed
    """
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

    def identity(payload):
        """
        Function that gets called when user has already authenticated, and Flask-JWT
        verified authorization header.
        :param payload: dictionary with identity key (users id)
        :return: a UserModel object
        """
        user_id = payload['identity']
        return UserModel.find_by_id()