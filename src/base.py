from google.appengine.api import users
import jinja2
import os
import settings
import webapp2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class _BaseHandler(webapp2.RequestHandler):
  def initialize(self, request, response):
    super(_BaseHandler, self).initialize(request, response)
    
    self.user = users.get_current_user()
    
    self.template_values = {'application_name':settings.APPLICATION_NAME,
                            'application_description':settings.APPLICATION_DESCRIPTION}
    
    if self.user:
      self.template_values.update({'user': self.user,
                                   'is_admin': users.is_current_user_admin(),
                                   'logout_url': users.create_logout_url('/')})
    else:
      self.template_values.update({'login_url': users.create_login_url(self.request.url)})

  def render(self, template):
    template = 'templates/' + template
    template = jinja_environment.get_template(template)
    self.response.out.write(template.render(self.template_values))