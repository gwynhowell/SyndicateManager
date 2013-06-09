import webapp2

import handlers
import settings

routes = [('/home', handlers.Home),
          ('/.*', handlers.Home)]

application = webapp2.WSGIApplication(routes, 
                                      debug=True, 
                                      config=settings.webapp2_config)