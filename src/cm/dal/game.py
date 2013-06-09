from cm.models import Game
from google.appengine.ext import ndb

def game_by_alias(alias):
  return ndb.Key(Game, alias).get()

def list_games(limit=100):
  return Game.query().order(Game.name).fetch(limit)

__all__ = [game_by_alias, list_games]