from webapp2_extras import sessions
import random
import string

def generate_csrf_token():
  session = sessions.get_store().get_session()
  if '_csrf_token' not in session:
    session['_csrf_token'] = random_string()
  return session['_csrf_token']

def random_string(size=6, chars=string.ascii_letters + string.digits):
  """ Generate random string """
  return ''.join(random.choice(chars) for _ in range(size))