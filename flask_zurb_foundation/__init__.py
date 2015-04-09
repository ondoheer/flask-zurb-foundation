# -*- coding: utf-8 -*-
"""
    flaskext.zurb_foundation
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Adds Foundation framework functionalities to flask

    :copyright: (c) 2015 by ondoheer.
    :license: BSD, see LICENSE for more details.
"""


__version__ = '0.2.1'
__version_info__ = __version__.split('.')
__author__ = 'Pedro Baumann'
__license__ = 'BSD'
__copyright__ = '(c) 2015 - Pedro Baumann.'

from flask import Blueprint


class Foundation(object):

    """
    :param: app: Flask aplication
    """

    def __init__(self,app=None):        

        if app:
            self.init_app(app)

    

    def init_app(self, app):

        self.app = app

        app.config.setdefault('FOUNDATION_MINIFIED', True)
        app.config.setdefault('FOUNDATION_CDN', False)
        app.config.setdefault('FOUNDATION_ICONS', True)
        app.config.setdefault('FOUNDATION_TEXT_DIRECTION', "ltr")
        app.config.setdefault('FOUNDATION_LANG', "en")

        
        blueprint = Blueprint(
            'foundation',
            __name__,
            static_folder='static',
            template_folder='templates',
            static_url_path=app.static_url_path + '/foundation',
        )

        app.register_blueprint(blueprint)

        

        

        if not hasattr(app, 'extensions'):
            app.extensions = {}
