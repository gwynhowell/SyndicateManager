from google.appengine.api import users
from webapp2_extras import jinja2
import dal
import re
import settings
import util
import webapp2

def jinja2_factory(app):
    j = jinja2.Jinja2(app)
    j.environment.filters.update({
        
    })
    j.environment.globals.update({
        'csrf_token': util.generate_csrf_token,
        'getattr': getattr,
        'str': str
    })
    return j

class _BaseHandler(webapp2.RequestHandler):
  def initialize(self, request, response):
    super(_BaseHandler, self).initialize(request, response)
    
    self.guser = users.get_current_user()
    
    self.template_values = {'application_name':settings.APPLICATION_NAME,
                            'application_description':settings.APPLICATION_DESCRIPTION}
    
    if self.guser:
      user = dal.user_by_email(self.guser.email())
      self.template_values.update({'user': user,
                                   'is_admin': users.is_current_user_admin(),
                                   'logout_url': users.create_logout_url('/')})
    else:
      self.template_values.update({'login_url': users.create_login_url(self.request.url)})

  @property
  def is_logged_in(self):
    return self.guser is not None
  
  @property
  def is_admin(self):
    return self.is_logged_in and users.is_current_user_admin() 

  def dispatch(self):
    if not self.is_logged_in:
      self.render('login.html')
    elif re.search('^/admin.*', self.request.path) and not self.is_admin:
      self.redirect('/')
    else:
      super(_BaseHandler, self).dispatch()

  @webapp2.cached_property
  def jinja2(self):
    return jinja2.get_jinja2(factory=jinja2_factory, app=self.app)

  def render(self, path, **kwargs):
    kwargs.update(self.template_values)
    self.response.write(self.jinja2.render_template(path, **kwargs))