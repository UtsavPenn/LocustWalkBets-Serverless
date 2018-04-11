import setup
from utils import responsify

from models import BetModel

def show(event, context):
	bets = []
	for bet in BetModel.scan():
		bets.append({'bet_id': bet.bet_id,
					'user_id': bet.user_id,
					'bet_amount':bet.bet_amount,
					'bet_for':bet.bet_for,
					'bet_paid_status':bet.bet_paid_status,
					'match_id': bet.match_id})

	return responsify(status_code=200, body={'bets': bets})




def create(event, context):
	pass

def update(event, context):
	pass

def delete(event, context):
	pass	
