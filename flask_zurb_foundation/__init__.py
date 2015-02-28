# -*- coding: utf-8 -*-
"""
    flaskext.zurb_foundation
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Description of the module goes here...

    :copyright: (c) 2015 by ondoheer.
    :license: BSD, see LICENSE for more details.
"""

from flask import Blueprint

class Foundation(object):
    def __init__(self, app=None):
        if app:
            self.init_app(app)


    def init_app(self, app):
        blueprint = Blueprint(
            'foundation',
            __name__,
            static_folder='static',
            template_folder='templates',
            static_url_path=app.static_url_path + '/foundation',
        )
        app.config.setdefault('FOUNDATION_CDN', 'local')
        


        app.register_blueprint(blueprint)

        if not hasattr(app, 'extensions'):
            app.extensions = {}
