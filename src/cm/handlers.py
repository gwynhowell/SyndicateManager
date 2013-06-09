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