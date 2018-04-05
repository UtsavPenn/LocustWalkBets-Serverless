import setup
from utils import jsonify

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute

class UserModel(Model):
    """
    A user identified by user_id
    """
    class Meta:
        table_name = 'UserInformationTable'
        region = 'us-east-1'
    user_id = UnicodeAttribute(hash_key=True)
    account_value = NumberAttribute()
    locked_value = NumberAttribute()


def show(event, context):
	users = []
	for user in UserModel.scan():
		users.append({'user_id': user.user_id,
					'account_value': user.account_value,
					'locked_value': user.locked_value})

	response = {
        "statusCode": 200,
        "body": jsonify({'users': users})
    }

	return response



def create(event, context):
	pass

def update(event, context):
	pass

def delete(event, context):
	pass	
