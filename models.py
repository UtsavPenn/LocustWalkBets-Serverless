from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute,BooleanAttribute


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


class MatchInfoModel(Model):
    """
    """
    class Meta:
        table_name = 'MatchInfoTable'
        region = 'us-east-1'
    match_id = NumberAttribute(hash_key=True)
    home_team = UnicodeAttribute()
    away_team = UnicodeAttribute()
    start_time = UnicodeAttribute()
    bets_processed = BooleanAttribute(default=False)
