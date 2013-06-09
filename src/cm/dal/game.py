from cm.models import Game

def game_by_alias(alias):
  return Game.query(Game.alias == alias).get()

def list_games(limit=100):
  return Game.query().order(Game.name).fetch(limit)

__all__ = [game_by_alias, list_games]