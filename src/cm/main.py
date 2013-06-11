# SyndicateManager
# /src/cm/main.py
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

from cm import admin
import handlers
import settings
import webapp2


routes = [
          webapp2.Route('/home', handlers.Home, 'home'),
          webapp2.Route('/syndicates', handlers.Syndicates, 'syndicates'),
          webapp2.Route('/create', handlers.Create, 'create'),          
          webapp2.Route('/syndicate', handlers.Syndicate, 'syndicate'),
          
          # admin handlers ...
          webapp2.Route('/admin/games', admin.Games, 'admin-games'),
          webapp2.Route('/admin/game/<alias:.*>', admin.Game, 'admin-game'),
          webapp2.Route('/admin/game', admin.Game, 'admin-create-game'),
          
          ('/.*', handlers.Home)]

application = webapp2.WSGIApplication(routes, 
                                      debug=True, 
                                      config=settings.webapp2_config)