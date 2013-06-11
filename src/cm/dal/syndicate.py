# SyndicateManager
# /src/cm/dal/syndicate.py
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

from cm.models import Syndicate, UserSyndicate
from google.appengine.ext import ndb

def syndicate_by_id(syndicate_id):
  return ndb.Key(Syndicate, long(syndicate_id)).get()

def list_user_syndicates_by_user_key(user_key, limit=100):
  query = UserSyndicate.query(UserSyndicate.user_key == user_key)
  query.order(UserSyndicate.syndicate_name)
  
  user_syndicates = query.fetch(limit)
  return user_syndicates

__all__ = [syndicate_by_id, list_user_syndicates_by_user_key]