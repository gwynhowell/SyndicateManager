from google.appengine.ext import ndb

class Game(ndb.Model):
  name = ndb.StringProperty()
  alias = ndb.StringProperty()
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
  first_name = ndb.StringProperty()
  last_name = ndb.StringProperty()
  email = ndb.StringProperty()

class Syndicate(ndb.Model):
  name = ndb.StringProperty()
  game = ndb.KeyProperty(kind=Game)
  manager = ndb.KeyProperty(kind=User)
  deputy_manager = ndb.KeyProperty(kind=User)
  
class Ticket(ndb.Model):
  numbers = ndb.IntegerProperty(repeated=True)
  
class UserSyndicate(ndb.Model):
  user = ndb.KeyProperty(kind=User)
  syndicate = ndb.KeyProperty(kind=Syndicate)
  
  # how much money the user has got in the kitty for this syndicate
  kitty = ndb.FloatProperty()
  
class UserDraw(ndb.Model):
  user = ndb.KeyProperty(kind=User)
  syndicate = ndb.KeyProperty(kind=Syndicate)
  draw = ndb.KeyProperty(kind=Draw)