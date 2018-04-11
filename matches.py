import setup
from utils import responsify
from models import MatchInfoModel



def show(event,context):
	matches = []
	for match in MatchInfoModel.scan():
		matches.append({	'match_id': match.match_id,
					'home_team': match.home_team,
					'away_team': match.away_team,
					'start_time': match.start_time,
					'bets_processed': match.bets_processed})

	return responsify(status_code=200, body={'matches': matches})
