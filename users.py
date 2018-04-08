import setup
from utils import responsify
from models import UserModel

def show(event, context):

    users = []
    for user in UserModel.scan():
        users.append({'user_id': user.user_id,
                      'account_value': user.account_value,
                      'locked_value': user.locked_value})

    users = sorted(users, key=lambda x: float(x['account_value']), reverse=True)
    for i, user in enumerate(users):
        user['standing'] = i + 1

    return responsify(status_code=200, body={'users': users})

