from cm.models import Syndicate, UserSyndicate
from google.appengine.ext import ndb

def syndicate_by_id(syndicate_id):
  return ndb.Key(Syndicate, syndicate_id).get()

def list_user_syndicates_by_user_key(user_key, limit=100):
  query = UserSyndicate.query(UserSyndicate.user_key == user_key)
  query.order(UserSyndicate.syndicate_name)
  
  user_syndicates = query.fetch(limit)
  return user_syndicates

__all__ = [syndicate_by_id, list_user_syndicates_by_user_key]