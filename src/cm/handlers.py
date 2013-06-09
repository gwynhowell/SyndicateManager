from base import _BaseHandler

class Home(_BaseHandler):
  def get(self):
    self.render('home.html')