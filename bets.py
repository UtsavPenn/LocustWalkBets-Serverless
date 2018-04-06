import setup
from utils import jsonify

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute

class BetModel(Model):
    """
    A bet identified by bet_id
    """
    class Meta:
        table_name = 'BetsTable'
        region = 'us-east-1'
    bet_id = UnicodeAttribute(hash_key=True)
    match_id =  NumberAttribute()
    user_id = UnicodeAttribute()
    bet_amount = NumberAttribute()
    bet_for = UnicodeAttribute()
    bet_paid_status = NumberAttribute()

def show(event, context):
	bets = []
	for bet in BetModel.scan():
		bets.append({'bet_id': bet.bet_id,
					'user_id': bet.user_id,
					'bet_amount':bet.bet_amount,
					'bet_for':bet.bet_for,
					'bet_paid_status':bet.bet_paid_status,
					'match_id': bet.match_id})

	response = {
        "statusCode": 200,
        "body": jsonify({'bets': bets})
    }

	return response



def create(event, context):
	pass

def update(event, context):
	pass

def delete(event, context):
	pass	
