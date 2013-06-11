# SyndicateManager
# /src/cm/util.py
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