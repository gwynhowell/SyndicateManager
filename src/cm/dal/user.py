# SyndicateManager
# /src/cm/dal/user.py
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