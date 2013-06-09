from google.appengine.ext import ndb

class Game(ndb.Model):
  name = ndb.StringProperty()
  description = ndb.StringProperty()
  price = ndb.FloatProperty()

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
  
class UserSyndicates(ndb.Model):
  user = ndb.KeyProperty(kind=User)
  syndicate = ndb.KeyProperty(kind=Syndicate)
  
class UserDraw(ndb.Model):
  user = ndb.KeyProperty(kind=User)
  syndicate = ndb.KeyProperty(kind=Syndicate)
  draw = ndb.KeyProperty(kind=Draw)