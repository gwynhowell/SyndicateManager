# SyndicateManager
# /src/cm/settings.py
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

APPLICATION_NAME = 'Syndicate Manager'
APPLICATION_DESCRIPTION = 'Syndicate Manager'
APPLICATION_VERSION = '0.1'
DEBUG = False
GOOGLE_ANALYTICS_ID = ''

webapp2_config = {
    'webapp2_extras.sessions': {'secret_key': 'FASDHJDASDHFASHDFAS'},
    'webapp2_extras.jinja2': {'template_path': ['templates'],
                              'environment_args': {'extensions': ['jinja2.ext.with_']}},
    'system_name': APPLICATION_NAME,
    'version': APPLICATION_VERSION,
    'debug_mode':DEBUG,
    'google_analytics_id':GOOGLE_ANALYTICS_ID }