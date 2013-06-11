# SyndicateManager
# /src/appogee/cache.py
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

"""
library to replicate the dynamic methods defined memcache
to prevent eclipse from incorrectly reporting errors throughout project
this file ensures all the [non]errors are contained in one place
"""

from google.appengine.api import memcache

ONE_HOUR_IN_SECONDS = 60 * 60
ONE_DAY_IN_SECONDS = ONE_HOUR_IN_SECONDS * 24

USER_TEAM_CAL_TIME = ONE_HOUR_IN_SECONDS

def get(key, namespace=None):
  """ Looks up a single key in memcache.
      Args:
          key: The key in memcache to look up. The Key can be a string or a tuple of (hash_value, string) where the hash_value, normally used for sharding onto a memcache instance, is instead ignored, as Google App Engine deals with the sharding transparently.
          namespace: An optional namespace for the key.
      Returns:
          The return value is the value of the key, if found in memcache, else None.
  """
  return memcache.get(key, namespace)

def set(key, value, time=0, min_compress_len=0, namespace=None):
  """ Sets a key's value, regardless of previous contents in cache.
      Args:
          key: Key to set. The Key can be a string or a tuple of (hash_value, string) where the hash_value, normally used for sharding onto a memcache instance, is instead ignored, as Google App Engine deals with the sharding transparently.
          value: Value to set. The value type can be any value supported by the Python pickle module for serializing values. The combined size of the serialized key and value must be at most 1 megabyte.
          time: Optional expiration time, either relative number of seconds from current time (up to 1 month), or an absolute Unix epoch time. By default, items never expire, though items may be evicted due to memory pressure. Float values will be rounded up to the nearest whole second.
          min_compress_len: Ignored option for compatibility.
          namespace: An optional namespace for the key.
      Returns:
          The return value is True if set, False on error.
  """
  return memcache.set(key, value, time, min_compress_len, namespace)

def add(key, value, time=0, min_compress_len=0, namespace=None):
  """ Sets a key's value, if and only if the item is not already in memcache.
      Args:
          key: Key to set. The Key can be a string or a tuple of (hash_value, string), where the hash_value, normally used for sharding onto a memcache instance is instead ignored, as Google App Engine deals with the sharding transparently.
          value: Value to set. The value type can be any value supported by the Python pickle module for serializing values. The combined size of the serialized key and value must be at most 1 megabyte.
          time: Optional expiration time, either relative number of seconds from current time (up to 1 month), or an absolute Unix epoch time. By default, items never expire, though items may be evicted due to memory pressure. Float values will be rounded up to the nearest whole second.
          min_compress_len: Ignored option for compatibility.
          namespace: An optional namespace for the key.
      Returns:
          The return value is True if set, False on error.
  """
  return memcache.add(key, value, time, min_compress_len, namespace)

def delete(key, seconds=0, namespace=None):
  """ Deletes a key from memcache.
      Args:
          key: Key to delete. A Key can be a string or a tuple of (hash_value, string), where the hash_value, normally used for sharding onto a memcache instance, is instead ignored, as Google App Engine deals with the sharding transparently.
          seconds: Optional number of seconds to make deleted items 'locked' for 'add' operations. Value can be a delta from current time (up to 1 month), or an absolute Unix epoch time. Defaults to 0, which means items can be immediately added. With or without this option, a 'set' operation will always work. Float values will be rounded up to the nearest whole second.
          namespace: An optional namespace for the key.
      Returns:
          The return value is 0 (DELETE_NETWORK_FAILURE) on network failure, 1 (DELETE_ITEM_MISSING) if the server tried to delete the item but didn't have it, and 2 (DELETE_SUCCESSFUL) if the item was actually deleted. This can be used as a boolean value, where a network failure is the only bad condition.
  """
  return memcache.delete(key, seconds, namespace)

def flush_all():
  """ Deletes everything in memcache.
      Returns:
          The return value is True on success, False on RPC or server error.
  """
  return memcache.flush_all()

def incr(key, delta=1, namespace=None, initial_value=None):
  """ Atomically increments a key's value. Internally, the value is a unsigned 64-bit integer.
      Memcache doesn't check 64-bit overflows. The value, if too large, will wrap around.
      
      If the key does not yet exist in the cache and you specify an initial_value, 
      the key's value will be set to this initial value and then incremented. 
      If the key does not exist and no initial_value is specified, the key's value will not be set.
      
      Args:
          key: Key to increment, or a list of keys to increment. Each Key can be a string or a tuple of (hash_value, string) where the hash_value, normally used for sharding onto a memcache instance, is instead ignored, as Google App Engine deals with the sharding transparently.
          delta: Non-negative integer value (int or long) to increment key by, defaulting to 1.
          namespace: An optional namespace for the key.
          initial_value: An initial value to be used if the key does not yet exist in the cache. Ignored if the key already exists. If None and the key does not exist, the key remains unset.
      Returns:
          The return value is a new long integer value, or None if key was not in the cache or could not be incremented for any other reason.
  """
  return memcache.incr(key, delta, namespace, initial_value)

def decr(key, delta=1, namespace=None, initial_value=None):
  """ Atomically decrements a key's value. Internally, the value is a unsigned 64-bit integer.
      Memcache doesn't check 64-bit overflows. The value, if too large, will wrap around.
      
      If the key does not yet exist in the cache and you specify an initial_value,
      the key's value will be set to this initial value and then decremented.
      If the key does not exist and no initial_value is specified, the key's value will not be set.
      
      Args:
          key: Key to decrement, or a list of keys to decrement. Each Key can be a string or a tuple of (hash_value, string), where the hash_value, normally used for sharding onto a memcache instance, is instead ignored, as Google App Engine deals with the sharding transparently.
          delta: Non-negative integer value (int or long) to decrement key by, defaulting to 1.
          namespace: An optional namespace for the key.
          initial_value: An initial value to be used if the key does not yet exist in the cache. Ignored if the key already exists. If None and the key does not exist, the key remains unset.
      Returns:
          The return value is a new long integer value, or None if key was not in the cache or could not be decremented for any other reason.
  """
  decr(key, delta=1, namespace=None, initial_value=None)
