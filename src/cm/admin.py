from cm import dal, models
from cm.base import _BaseHandler

class Games(_BaseHandler):
  def get(self):
    self.template_values['games'] = dal.list_games()
    self.render('admin/games.html')
    
class Game(_BaseHandler):
  def get(self, alias=None):
    if alias:
      game = dal.game_by_alias(alias)
      self.template_values['game'] = game
      self.template_values['form_url'] = self.uri_for('admin-game', alias=alias)
    else:
      self.template_values['form_url'] = self.uri_for('admin-create-game')
      
    self.render('admin/game.html')
    
  def post(self, alias=None):
    alias = alias or self.request.get('alias')
    name = self.request.get('name')
    description = self.request.get('description')
    price = self.request.get('price')
    draws = self.request.get_all('draws')
    
    game = models.Game.get_or_insert(alias,
                                     alias=alias)
    game.name = name
    game.description = description
    game.price = float(price)
    game.draws = [int(draw) for draw in draws]
    game.put()
    
    self.redirect_to('admin-games')