from appogee import cache
from cm import models

def user_by_email(email):
  """ load a user object by email
      Args:
        email: the email address of the user to load
      Returns:
        the user object. if email does not exist, a new user entity is created, and returned
  """
  user = cache.get(email.lower())
  if not user:
    user = models.User.get_or_insert(email.lower())
    
    # cache for 10 minutes
    cache.set(email.lower(), user, 60 * 10)
  return user
  
__all__ = [user_by_email]