#!/usr/bin/env python2
# coding=utf8

__version__ = '5.5.1'

from flask import Blueprint, current_app, url_for

try:
    from wtforms.fields import HiddenField
except ImportError:
    def is_hidden_field_filter(field):
        raise RuntimeError('WTForms is not installed.')
else:
    def is_hidden_field_filter(field):
        return isinstance(field, HiddenField)


class CDN(object):

    """Base class for CDN objects."""

    def get_resource_url(self, filename):
        """Return resource url for filename."""
        raise NotImplementedError


class StaticCDN(object):

    """A CDN that serves content from the local application.

    :param static_endpoint: Endpoint to use.
    :param rev: If ``True``, honor ``BOOTSTRAP_QUERYSTRING_REVVING``.
    """

    def __init__(self, static_endpoint='static'):
        self.static_endpoint = static_endpoint

    def get_resource_url(self, filename):
        extra_args = {}

        return url_for(self.static_endpoint, filename=filename, **extra_args)


class ConditionalCDN(object):

    """Serves files from one CDN or another, depending on whether a
    configuration value is set.

    :param confvar: Configuration variable to use.
    :param primary: CDN to use if the configuration variable is ``True``.
    :param fallback: CDN to use otherwise.
    """

    def __init__(self, confvar, primary, fallback):
        self.confvar = confvar
        self.primary = primary
        self.fallback = fallback

    def get_resource_url(self, filename):
        if current_app.config[self.confvar]:
            return self.primary.get_resource_url(filename)
        return self.fallback.get_resource_url(filename)


class Foundation(object):

 	def __init__(self, app=None):
 		if app is not None:
 			self.init_app(app)

 	def init_app(self, app):
 		FOUNDATION_VERSION = __version__
 		JQUERY_VERSION = '2.1.3'

 		blueprint = Blueprint(
                    'foundation',
                    __name__,
                    template_folder='templates',
                    static_folder=app.static_url_path + 'foundation'
 		)

 		app.register_blueprint(blueprint)

 		app.jinja_env.globals['foundation_is_hidden_field'] = is_hidden_field_filter

 		if not hasattr(app, 'extentions'):
 			app.extentions = {}

 		local = StaticCDN('foundation.static')
 		static = StaticCDN()
 		jquery = 'foundation.static'

 		


 		app.extensions['foundation'] = {
 			'cdns': {
 				'local': local,
 				'static': static,
 				'jquery': jquery,
 			}
 		}

