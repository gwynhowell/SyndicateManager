# SyndicateManager
# /src/cm/admin.py
#
# Copyright (c) 2013 Gwyn Howell
#
# LICENSE:
#
# This file is part of SyndicateManager (http://my-syndicate.appspot.com).
#
# SyndicateManager is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 2 of the License, or (at your option) any
# later version.
#
# SyndicateManager is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with SyndicateManager.  If not, see
# <http://www.gnu.org/licenses/>.
#
#
# @author Gwyn Howell <gwyn[at]howellmail[dot]co[dot]uk>
# @license http://www.gnu.org/licenses/gpl.html
# @copyright 2013 Gwyn Howell

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
    
    game = models.Game.get_or_insert(alias)
    game.name = name
    game.description = description
    game.price = float(price)
    game.draws = [int(draw) for draw in draws]
    game.put()
    
    self.redirect_to('admin-games')