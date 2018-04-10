import setup
from utils import responsify
from models import MatchInfoModel



def show(event,context):
	matches = []
	for match in MatchInfoModel.scan():
		matches.append({#	'match_id': MatchInfoModel.match_id,
					'home_team': MatchInfoModel.home_team,
					'away_team': MatchInfoModel.away_team,
					'start_time': MatchInfoModel.start_time,
					'bets_processed': MatchInfoModel.bets_processed})

	return responsify(status_code=200, body={'matches': matches})
