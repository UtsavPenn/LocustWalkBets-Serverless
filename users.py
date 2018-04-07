import setup
from utils import jsonify

from models import UserModel


def show(event, context):
    users = []
    for user in UserModel.scan():
        users.append({'user_id': user.user_id,
                      'account_value': user.account_value,
                      'locked_value': user.locked_value})

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": jsonify({'users': users})
    }

    return response


def create(event, context):
    pass


def update(event, context):
    pass


def delete(event, context):
    pass
