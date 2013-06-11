# SyndicateManager
# /src/cm/handlers.py
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

from base import _BaseHandler
from cm import dal, models
from google.appengine.ext import ndb

class Home(_BaseHandler):
  def get(self):
    self.render('home.html')

class Syndicates(_BaseHandler):
  menu = 'Syndicates'
  
  def get(self):
    syndicates = dal.list_user_syndicates_by_user_key(self.user.key)
    self.template_values['syndicates'] = syndicates
    self.render('syndicates.html')
    
class Create(_BaseHandler):
  menu = 'Create'
  
  def get(self):
    self.template_values['games'] = dal.list_games()
    self.render('create.html')
  
  def post(self):
    name = self.request.get('name')
    game_alias = self.request.get('game')
    
    game_key = ndb.Key(models.Game, game_alias)
    
    syndicate = models.Syndicate(name=name,
                                 game_key=game_key,
                                 manager_key=self.user.key)
    syndicate.put()
    
    models.UserSyndicate(user_key=self.user.key,
                         syndicate_key=syndicate.key,
                         status='Approved').put()
    
    self.redirect_to('syndicate',
                     id=syndicate.key.id())
    
class Syndicate(_BaseHandler):
  menu = 'Syndicates'
  
  def get(self):
    syndicate_id = self.request.get('id')
    syndicate = dal.syndicate_by_id(syndicate_id)
    self.template_values['syndicate'] = syndicate
    self.render('syndicate.html')