from cm import admin
import handlers
import settings
import webapp2


routes = [('/home', handlers.Home),
          
          # admin handlers ...
          webapp2.Route('/admin/games', admin.Games, 'admin-games'),
          webapp2.Route('/admin/game/<alias:.*>', admin.Game, 'admin-game'),
          webapp2.Route('/admin/game', admin.Game, 'admin-create-game'),
          
          ('/.*', handlers.Home)]

application = webapp2.WSGIApplication(routes, 
                                      debug=True, 
                                      config=settings.webapp2_config)