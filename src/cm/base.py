# SyndicateManager
# /src/cm/base.py
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

from google.appengine.api import users
from webapp2_extras import jinja2
import dal
import re
import settings
import util
import webapp2

def format_currency(value):
#  return "${:,.2f}".format(value)
  return "&pound;{:,.2f}".format(value)

def jinja2_factory(app):
    j = jinja2.Jinja2(app)
    j.environment.filters.update({
        'format_currency': format_currency
    })
    j.environment.globals.update({
        'csrf_token': util.generate_csrf_token,
        'getattr': getattr,
        'str': str,
        'uri_for': webapp2.uri_for
    })
    return j

class _BaseHandler(webapp2.RequestHandler):
  menu = ''
  
  def initialize(self, request, response):
    super(_BaseHandler, self).initialize(request, response)
    
    self.guser = users.get_current_user()
    
    self.template_values = {'application_name':settings.APPLICATION_NAME,
                            'application_description':settings.APPLICATION_DESCRIPTION}
    
    if self.guser:
      self.user = dal.user_by_email(self.guser.email())
      self.template_values.update({'user': self.user,
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
    self.template_values['menu'] = self.menu
    kwargs.update(self.template_values)
    self.response.write(self.jinja2.render_template(path, **kwargs))