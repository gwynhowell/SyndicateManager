from google.appengine.ext import ndb

class Game(ndb.Model):
  name = ndb.StringProperty()
  description = ndb.StringProperty()
  draws = ndb.IntegerProperty(repeated=True)
  price = ndb.FloatProperty()
  
  @property
  def draw_sun(self):
    return 0 in self.draws
  
  @property
  def draw_mon(self):
    return 1 in self.draws
  
  @property
  def draw_tue(self):
    return 2 in self.draws
  
  @property
  def draw_wed(self):
    return 3 in self.draws
  
  @property
  def draw_thu(self):
    return 4 in self.draws
  
  @property
  def draw_fri(self):
    return 5 in self.draws
  
  @property
  def draw_sat(self):
    return 6 in self.draws

class Draw(ndb.Model):
  date = ndb.DateProperty()
  numbers = ndb.IntegerProperty(repeated=True)
  
class User(ndb.Model):
  nickname = ndb.StringProperty()
  first_name = ndb.StringProperty()
  last_name = ndb.StringProperty()

  @property
  def email(self):
    return self.key.id()

  @property
  def display_name(self):
    if self.nickname:
      return self.nickname
    elif self.first_name and self.last_name:
      return ' '.join([self.first_name, self.last_name])
    else:
      return self.email

class Syndicate(ndb.Model):
  name = ndb.StringProperty()
  game_key = ndb.KeyProperty(kind=Game)
  manager_key = ndb.KeyProperty(kind=User)
  deputy_manager_key = ndb.KeyProperty(kind=User)
  
  # denormalized values
  game_name = ndb.StringProperty()
  manager_name = ndb.StringProperty()
  
  def _pre_put_hook(self):
    ndb.Model._pre_put_hook(self)
    
    game = self.game_key.get()
    manager = self.manager_key.get()
    
    self.game_name = game.name
    self.manager_name = manager.display_name
  
class Ticket(ndb.Model):
  numbers = ndb.IntegerProperty(repeated=True)
  
class UserSyndicate(ndb.Model):
  user_key = ndb.KeyProperty(kind=User)
  syndicate_key = ndb.KeyProperty(kind=Syndicate)
  
  # how much money the user has got in the kitty for this syndicate
  status = ndb.StringProperty(choices=['Invited',     # a manager has invited user to the syndicate, but they haven't accepted
                                       'Pending',     # a user has entered a code to join a syndicate, but the manager hasn't approved
                                       'Approved'])   # a user who is a member of a syndicate
  kitty = ndb.FloatProperty(default=0.0)
  
  # denormalized values
  user_name = ndb.StringProperty()
  syndicate_name = ndb.StringProperty()
  game_name = ndb.StringProperty()
  
  def _pre_put_hook(self):
    ndb.Model._pre_put_hook(self)
    
    user = self.user_key.get()
    syndicate = self.syndicate_key.get()
    
    self.user_name = user.display_name
    self.syndicate_name = syndicate.name
    self.game_name = syndicate.game_name
  
class UserDraw(ndb.Model):
  user_key = ndb.KeyProperty(kind=User)
  syndicate_key = ndb.KeyProperty(kind=Syndicate)
  draw_key = ndb.KeyProperty(kind=Draw)