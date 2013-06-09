APPLICATION_NAME = 'Syndicate Manager'
APPLICATION_DESCRIPTION = 'Syndicate Manager'
APPLICATION_VERSION = '0.1'
DEBUG = False
GOOGLE_ANALYTICS_ID = ''

webapp2_config = {
    'webapp2_extras.sessions': {'secret_key': 'BDFJ3487N832NE9'},
    'webapp2_extras.jinja2': {'template_path': ['templates'],
                              'environment_args': {'extensions': ['jinja2.ext.i18n', 'jinja2.ext.with_']}},
    'system_name': APPLICATION_NAME,
    'version': APPLICATION_VERSION,
    'debug_mode':DEBUG,
    'google_analytics_id':GOOGLE_ANALYTICS_ID }